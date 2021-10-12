#!/usr/bin/env python
#from __future__ import print_function
from flask import Flask
from flask import request
import os, json
import requests

app = Flask(__name__)

#WEBEX API URL

url = "https://api.ciscospark.com/v1/messages"

#ENVIRONMENTAL VARIABLES - MUST BE DEFINED IN AWS LAMBDA, ADDITIONAL ENCRYPTION POSSIBLE

roomid = os.environ['ROOMID']
auth = os.environ['AUTH']

#DON'T FORGET TO CHANGE DEFAULT LAMBDA HANDLER IN AWS GUI. IT SHOULD BE "webhook-listener.lambda_handler"
        
def lambda_handler(dnac, event):

    body = json.loads(dnac['body'])

    """
    This is a subject of change. I have chosen only following parameters from the webhook which are posted in WebEx room.
    """

    event_name = body['details']['Assurance Issue Name']
    time = dnac['requestContext']['requestTime']
    category = body['category']
    details = body['details']['Assurance Issue Details']

    if 'Location' in body['details']:
        location = body['details']['Location']
    else:
        location = "N/A"

    #This is only for testing purpose to see how the entire Webhook looks like in AWS CloudWatch - might be commented
    #print(dnac)
    
    message = "******** ALERT CISCO DNA CENTER ************\n\n" + "EVENT : " + event_name + "\n\n" + "TIME : " + time + "\n\n" + "CATEGORY : " + category + "\n\n" + "DETAILS : " + details +  "\n\n" + "LOCATION : " + location

    #Posting a message to WebEx room
    post_message(message)

    return { "statusCode": 200 }


def post_message(message):

    #ENVIRONMENT VARIABLES USED HERE

    if auth == "Bearer XXXX":
        print("No WebexTeams Token")
        return
    payload = {"roomId" : roomid,"text" : message}
    headers = {
    'authorization': auth,
    'content-type': "application/json"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

@app.route('/', defaults={'path': ''}, methods=['GET','POST'])
@app.route('/<path:path>', methods=["GET","PUT","POST","DELETE"])
def get_all(path):
    print("Method {}, URI {}".format(request.method,path))
    if request.method == "POST":
        print (request.headers)
        print (request.json)
        if request.json != {}:
            lambda_handler(request.remote_addr, request.json)
        else:
            print("skipping - empty")
    return ("OK")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9000", ssl_context='adhoc')