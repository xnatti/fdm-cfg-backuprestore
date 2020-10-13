#!/usr/bin/env python3
# 
# This snippet can be used to list config files on the FDM.
# Cisco's guide with cURL examples: https://www.cisco.com/c/en/us/td/docs/security/firepower/ftd-api/guide/ftd-rest-api/ftd-api-import-export.html
#

import requests
import json
from getpass import getpass

# Disable insecure request warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# To upload a config file file with cURL:
# curl -kivv -F 'fileToUpload=@./Exported-at-newconfig.txt' -H "Authorization: Bearer XXXXXXXXXX" https://FDM/api/fdm/latest/action/uploadconfigfile
# pay attention to diskFileName



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



# to list files: 
response = requests.get('https://' + FDMHost + '/api/fdm/latest/action/configfiles', headers=headers, verify=False)
print(response.text)
