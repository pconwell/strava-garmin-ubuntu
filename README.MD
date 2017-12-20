> This is still a work in progress. The script itself works perfectly fine, but I haven't finished the part of the program that will automatically configure your authentication keys. If you know what you are doing, you need to generate an oauth key and place that key in the config.ini file under 'authenication' 'token' = 

## Overview

## How to use this script

### Set up API Token
The script itself is fairly easy. The hardest part is setting up correct access to the Strava API.

1. Go to https://developers.strava.com/ and create an app
2. It doesn't matter what you enter into the fields EXCEPT the Authorization Callback Domain *must* be `localhost:8000`
3. The only things you will need is the 'Client ID' and the 'Client Secret'
4. Rename the config.ini.template file to config.ini and open the file
5. Copy and paste your `Client ID` and `Client Secret`\* into the appropriate fields.
6. The only other setting you may need to adjust is the \[RANGE\] 'days' setting. This is how many days into the past it will upload data (assuming it has not already been uploaded to Strava). This is to prevent you from accidentally uploading a whole bunch of duplicate runs from a long time ago.

> I still need to finish this last little part of the program. Here is where you need to generate your oauth token. It's farily simple, I just haven't finished the code yet. Basically, you need to make a request such as:

> curl -X POST https://www.strava.com/oauth/token -F client_id=22111 -F client_secret=YOUR_SECRETE -F code=YOUR_CODE

> The YOUR_CODE part can be found by going to:

>https://www.strava.com/oauth/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=http://localhost:8000&approval_prompt=force&scope=view_private,write

> Make sure to replace YOUR_CLIENT_ID with your client. Click 'Authorize' and it will take you to a dead webpage BUT, what you need to the URL of the webpage that it redirected you to. It'll look something like:

> http://localhost:8000/?state=&code=601e3e3721fc93ca87d03c8e16e940ef5d99c7b8

> The 601e3e3721fc93ca87d03c8e16e940ef5d99c7b8 part is your code. Take the code and your secret and put them in the curl command, which will generate your oauth token. The Token then goes into the config.ini file.

\* It should go without saying that the secret is just that - a secret. Do not share it with anyone.


### Setting up your computer

This script assumes that your garmin device mounts to `/media/$USER/GARMIN/GARMIN/`. If your device mounts somewhere else, you will need to find that location and change line 18 of `garmin.py`

### Uploading data
Pretty simple:

`$ python3 garmin.py`

That's it. It will check what workouts you have already uploaded and upload any that are missing. You could probably set up a cronjob to run the script every night, or if someone is really smart they could probably figure out how to run this script each time the watch is connected to the computer.
