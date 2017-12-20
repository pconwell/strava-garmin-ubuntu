import os
import datetime
import configparser
import requests
import webbrowser

import webserver

# Read authentication from config file and some intial setup
config = configparser.ConfigParser()
config.read(['./config.ini'])

strava_secret = config['USER']['client_secret']
strava_cid = config['USER']['client_id']
strava_token = config['Authentication']['token']

user = os.getlogin()
fpath = "/media/" + user + "/GARMIN/GARMIN/ACTIVITY"

# Read activities currently on garmin device
# Each activity is initially marked with "no" meaning it has not yet been
# uploaded. A further bit down, we will actually check if it's been uploaded
# then change "no" to "yes" as necessary.
garmin_activity = []
for i in os.listdir(fpath):
    garmin_activity.append([i, datetime.datetime.utcfromtimestamp(os.path.getmtime(fpath + f"/{i}")), "no"])
garmin_activity.sort(key=lambda x: x[1])

# Check if auth token exists. If not, ask for authentication and generate one
# This section needs to be finished, it's only about half done...
if strava_token == "":
    webbrowser.open_new_tab(f'https://www.strava.com/oauth/authorize?client_id={strava_cid}&response_type=code&redirect_uri=http://localhost:8000&approval_prompt=force&scope=view_private,write')
    webserver.run()

# Set up http header with users auth token, nothing special here
headers = {
    'Authorization': f'Bearer {strava_token}',
}

# Now we check the Strava website to see what activites have already been
# uploaded. If the activity has already been uploaded, "no" is changed to "yes"
response = requests.get('https://www.strava.com/api/v3/athlete/activities', headers=headers)

for i in response.json():
    for a in garmin_activity:
        if a[0].lower() == i['external_id'].lower():
            a.pop()
            a.append('yes')

# Checks to see if 1) the activity is within a set range (see config file), and
# checks to see if the activity is tagged with a "no", meaning is hasn't been
# uploaded yet. NOTE: The day range that is set in the config file is a fail
# safe so you don't accidentally upload really old workouts that were deleted
# previously. The date range can be set to anything you want, but as long as you
# plug your watch up to the computer after every workout, a range of 7 days is
# probably pretty logical. Just be aware, if you set it to 7 (for example), but
# don't plug your watch up till day 8, whatever workouts happened 8+ days ago
# will not be uploaded.
upload = []
for i in garmin_activity:
    if i[1] > (datetime.datetime.today() - datetime.timedelta(int(config['RANGE']['days']))) and i[2] == 'no':
        upload.append(i)


# Upload the files to Strava
for i in upload:
        print(i[0])
        files = {
            'file': (i[0], open(f"{fpath}/{i[0]}", 'rb')),
            'data_type': (None, 'fit'),
        }

        response = requests.post('https://www.strava.com/api/v3/uploads', headers=headers, files=files)
