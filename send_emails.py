from __future__ import print_function
import openpyxl

import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
# Instantiate the client\
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = ''
api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
# Load Excel workbook
workbook = openpyxl.load_workbook('contacts.xlsx')
sheet = workbook.active

# Get email addresses from the sheet
emails = [cell.value for cell in sheet['A']]

# Define the campaign settin
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
name= "Campaign sent via the API",
subject= "My subject",
sender= { "name": "Jude oyedele", "email": "judeokennywise@gmail.com"},
# Content that will be sent\
html_content= "Congratulations! You successfully sent this example campaign via the Sendinblue API.",
# Select the recipients\
recipients= {"segmentIds": [1]},
# Schedule the sending in one hour\
scheduled_at= "2023-04-27 13:15:01"
)

try:
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)