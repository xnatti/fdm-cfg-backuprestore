#!/usr/bin/env python3

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

# populating the variables)

print('Firepower Host(IP): ', end='')
FDMHost = input()

print('Username: ', end='')
username = input()

# getpass prints "Password:" on it's own
password = getpass()


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



importBody = {
 'diskFileName': 'Exported-at-newconfig.txt',
 'preserveConfigFile': True,
 'autoDeploy': False,
 'allowPendingChange': True,
 'type': 'scheduleconfigimport'
}

#to load config response = requests.post('https://192.168.250.10/api/fdm/latest/action/configimport', data=json.dumps(importBody), headers=headers, verify=False)
# may loose admin access for a while

# to list files: response = requests.get('https://192.168.250.10/api/fdm/latest/action/configfiles', headers=headers, verify=False)
