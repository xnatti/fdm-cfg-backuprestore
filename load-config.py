#!/usr/bin/env python3
#
# This snippet just loads the selected config.
# Auto deploy is off, so you must deploy manually
#
import requests
import json
from getpass import getpass


# ok, actually to upload the friggin file:
# curl -kivv -F 'fileToUpload=@./Exported-at-newconfig.txt' -H "Authorization: Bearer XXXXXXXXXX" https://FDM/api/fdm/latest/action/uploadconfigfile
# pay attn to diskFileName



headers = {
 'Accept': 'application/json',
 'Content-Type': 'application/json'
}

username = ''
password = ''
FDMHost = ''

# populating the variables

print('Firepower Host(IP): ', end='')
FDMHost = input()

print('Username: ', end='')
username = input()

# getpass prints "Password:" on it's own
password = getpass()

print('File name according to FDM (diskFileName): ', end='')
diskFileName = input()

headers = {
 'Accept': 'application/json',
 'Content-Type': 'application/json'
}

def newToken():
 FDMAuth = 'https://' + FDMHost + '/api/fdm/latest/fdm/token'
 fdm_password_grant = {
  'grant_type': 'password',
  'username': username,
  'password': password
 }
 response = requests.post(FDMAuth, data=json.dumps(fdm_password_grant), headers=headers, verify=False)
 responseJSON = json.loads(bytes.decode(response.content))
 headers['Authorization'] = 'Bearer ' + responseJSON['access_token']

newToken()

importBody = {
 'diskFileName': diskFileName,
 'preserveConfigFile': True,
 'autoDeploy': False,
 'allowPendingChange': True,
 'type': 'scheduleconfigimport'
}

# loading the config on FDM. Note that you may loose admin access for a few minutes while the FDM is working on this.
response = requests.post('https://' + FDMHost + '/api/fdm/latest/action/configimport', data=json.dumps(importBody), headers=headers, verify=False)

# print the response, should be 200.
print(response)
