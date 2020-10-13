#!/usr/bin/env python3
# 
# A simple script to fetch or import configs from FirePower 6.5 devices
# Related doc: https://www.cisco.com/c/en/us/td/docs/security/firepower/ftd-api/guide/ftd-rest-api/ftd-api-import-export.html
# jonatan@routing.is
# mkey

from getpass import getpass
import requests
import json
import time

from requests import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable insecure request warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)





# presetting the variables (b/c testing)
username = ''
password = ''
FDMHost = ''

# populating the variables)

print('Firepower Host(IP): ', end='')
FDMHost = input()

print('Username: ', end='')
username = input()

# getpass prints "Password:" on it's own
password = getpass()


# base URI for exporting config
FDMExport = 'https://' + FDMHost + '/api/fdm/latest/action/configexport'

# base URI for authentication to get token info
FDMAuth = 'https://' + FDMHost + '/api/fdm/latest/fdm/token'

# base URI for checking job export status
FDMJob = 'https://' + FDMHost + '/api/fdm/latest/jobs/configexportstatus'

# base URI for download function
FDMDownload = 'https://' + FDMHost + '/api/fdm/latest/action/downloadconfigfile/'



headers = {
 'Accept': 'application/json',
 'Content-Type': 'application/json'
}


# dict/json object to use for token generation
fdm_password_grant = {
 'grant_type': 'password',
 'username': username,
 'password': password
}


#getting the token info from FDM and loading into a dict
# atn, verify False, needs cert check
response = requests.post(FDMAuth, data=json.dumps(fdm_password_grant), headers=headers, verify=False)
responseJSON = json.loads(bytes.decode(response.content))

# need to check if successful


#adding token to the header
headers['Authorization'] = 'Bearer ' + responseJSON['access_token']


exportBody = {
 'doNotEncrypt': True,
 'configExportType': 'FULL_EXPORT',
 'deployedObjectsonly': True,
 'type': 'scheduleconfigexport'
}


# here we post the config backup job
response = requests.post(FDMExport, json.dumps(exportBody), headers=headers, verify=False)
responseJSON = json.loads(bytes.decode(response.content))

jobDetails = {
 'jobID': responseJSON['jobHistoryUuid']
}

 
# wait time for job
print('Waiting 15 sec for job to maybe finish...')
time.sleep(15)


# I can use FDMJob variable to look into all jobs, or use specific job info from the FDMExport output

response = requests.get(FDMJob + '/' + jobDetails['jobID'], headers=headers, verify=False)
responseJSON = json.loads(bytes.decode(response.content))

if responseJSON['status'] == 'SUCCESS':
 print('Job finished, lets get that file')

jobDetails['filename'] = responseJSON['diskFileName']

# getting a new copy of the headers and modifying the accept attribute since we are downloading a binary file and not just text
headersStream = headers.copy()
headersStream['Accept'] = 'application/octet-stream'


# actual download of the config
response = requests.get(FDMDownload + jobDetails['filename'], headers=headersStream, verify=False)

if response.status_code == 200:
 print('Download successful')

# saving the config to a zip file
print('Attempting to write to ' + jobDetails['filename'])

with open(jobDetails['filename'], 'wb') as file:
 file.write(response.content)
