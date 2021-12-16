# Sending Webhooks from Cisco DNA Center to WebEx room with AWS Lambda

This is a repo for handling DNAC Webhook by AWS Lambda and sending notifications to Cisco WebEx

****************

DON'T FORGET ABOUT INSTALLING REQUIRED DEPENDENCIES AND UPLOADING ZIP FILE TO AWS LAMBDA!
https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

****************

DON'T FORGET TO CHANGE DEFAULT LAMBDA HANDLER TO "webhook-listener.lambda_handler"

****************

Starting from version 2.2.3.3, Cisco DNA Center natively integrates with Cisco WebEx, so there is no need for deploying external Webhook Listener anymore. Nevertheless, this code can be used for sending notifications to other systems (e.g. Slack).
