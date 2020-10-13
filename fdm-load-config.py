#!/usr/bin/env python3
#
# This snippet just loads the selected config.
# Auto deploy is off, so you must deploy manually
# Cisco's guide with cURL examples: https://www.cisco.com/c/en/us/td/docs/security/firepower/ftd-api/guide/ftd-rest-api/ftd-api-import-export.html
#
import requests
import json
from getpass import getpass


# Disable insecure request warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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

