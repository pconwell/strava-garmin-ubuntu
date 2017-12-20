## Overview

## How to use this script

### Set up API Token
The script itself is fairly easy. The hardest part BY FAR is setting up correct access to the Strava API.

1. Go to https://developers.strava.com/ and create an app
2. It doesn't really matter what you fill in as you are only making this app for your own personal use.
3. The only things you will need is the 'Client ID' and the 'Client Secret'
4. Go to the following webpage: https://www.strava.com/oauth/authorize?client_id=5555&response_type=code&redirect_uri=http://127.0.0.1&scope=view_private,write&approval_prompt=force
5. Make sure to change the 'client_id=' to your client_id. In this example, the client_id is 5555, but the 5555 needs to be changed to YOUR client_id which can be found at https://www.strava.com/settings/api after you create your app in step 1 above.
6. Click 'Authorize'
7. This is important! You will now see a 'broken' webpage. We don't care about the webpage, but look at the address bar and you should see something like http://127.0.0.1/?state=&code=e3882cba1e4b7cbbb39abdfda5517180c34518cc
8. We need the code (the part after 'code=', in this example it is 'e3882cba1e4b7cbbb39abdfda5517180c34518cc')
9. Open a terminal and enter the following:

curl -X POST https://www.strava.com/oauth/token -F client_id=5555 -F client_secret=c98a0622df6ab584f23ff11147b79f5e5c69e5b6 -F code=e3882cba1e4b7cbbb39abdfda5517180c34518cc

10. Make sure to replace the client_id with YOUR client_id and the client_secret with YOUR client_secret
11. You should see a long response in your terminal window. The only thing we are worried about is the "access_token":"7885382d3269b1dfecdd6932a0fbcc8759df75a7" part. Your access token will be different than the example shown here. Save your access token to a safe place and keep it secret. The access token is just like a password to your account.

Once you have your access token, the hard part is over.

### Setting up your computer

### Uploading data
