import os
import datetime
import configparser
import requests

# Read authentication from config file
config = configparser.ConfigParser()
config.read(['./config.ini'])

strava_key = config['AUTH']['strava_key']
strava_token = config['AUTH']['strava_token']

# 
user = os.getlogin()
fpath = "/media/" + user + "/GARMIN/GARMIN/ACTIVITY"

activity = []
for i in os.listdir(fpath):
    activity.append([i, datetime.datetime.utcfromtimestamp(os.path.getmtime(fpath + f"/{i}"))])

activity.sort(key=lambda x: x[1])

# # create permenant record of all activities
# db = sqlite3.connect('activity.sql')
# c = db.cursor()
#
# # Check if table 'activity' exists
# c.execute(''' SELECT count(*) FROM sqlite_master WHERE type = "table" AND name = "activity" ''')
#
# if c.fetchone()[0] == True:
#     print("Table exists, skipping...")
# else:
#     # Create table and insert all current activites
#     print("Generateing Table")
#     c.execute(''' CREATE TABLE activity(id INTEGER PRIMARY KEY, name TEXT, run_datetime DATETIME)''')
#     c.executemany(''' INSERT INTO activity(name, run_datetime) VALUES(?,?) ''', activity)
#     db.commit()
#
# c.execute('''SELECT name, run_datetime FROM activity''')
# for row in c:
#     # Limit results to past 4 weeks (28 days)
#     # This SHOULD prevent duplicates being uploaded to strava when the watch
#     # automatically deletes old records
#     if datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S") > (datetime.datetime.today() - datetime.timedelta(28)):
#         if row[0] in os.listdir(fpath):
#             print(f"{row[0]} {row[1]} already exists in records, skipping...")
#         else:
#             print("New workout found!")
#             print(f"    Uploading: {row[0]} {row[1]} to Strava Servers (replace API code here)")
#             print(f"    Saving:    {row[0]} {row[1]} to local database (replace code here)")
#             print("    Success!")
#
# db.close()

headers = {
    'Authorization': f'Bearer {strava_token}',
}

# response = requests.get('https://www.strava.com/api/v3/athlete', headers=headers)
#
# for i in response.json():
#     print(i, response.json()[i])

# Past 28 days of activity
response = requests.get('https://www.strava.com/api/v3/athlete/activities', headers=headers)

for i in response.json():
    if datetime.datetime.strptime(i['start_date_local'], "%Y-%m-%dT%H:%M:%SZ") > (datetime.datetime.today() - datetime.timedelta(28)):
        print(i['start_date_local'], i['external_id'])

# # Upload
# files = {
#     'file': ('7CI60334.FIT', open(f"{fpath}/7CI60334.FIT", 'rb')),
#     'data_type': (None, 'fit'),
# }
#
# response = requests.post('https://www.strava.com/api/v3/uploads', headers=headers, files=files)
