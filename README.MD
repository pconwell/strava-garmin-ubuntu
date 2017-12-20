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

\* It should go without saying that the secret is just that - a secret. Do not share it with anyone.


### Setting up your computer

This script assumes that your garmin device mounts to `/media/$USER/GARMIN/GARMIN/`. If your device mounts somewhere else, you will need to find that location and change line 18 of `garmin.py`

### Uploading data
Pretty simple:

`$ python3 garmin.py`

That's it. It will check what workouts you have already uploaded and upload any that are missing. You could probably set up a cronjob to run the script every night, or if someone is really smart they could probably figure out how to run this script each time the watch is connected to the computer.
