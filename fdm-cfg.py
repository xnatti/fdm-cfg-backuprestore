#!/usr/bin/env python3
# 
# A simple script to fetch or import configs from FirePower 6.5 devices
# Related doc: https://www.cisco.com/c/en/us/td/docs/security/firepower/ftd-api/guide/ftd-rest-api/ftd-api-import-export.html
# jonatan@routing.is
# mkey

from getpass import getpass
import requests
import json

username = ''
password = ''
FDMHost = ''

print('Firepower Host: ', end='')
FDMHost = input()

print('Username: ', end='')
username = input()

# getpass prints "Password:" on it's own
password = getpass()


# base URI for exporting config
FDMExport = 'https://' + FDMHost + '/api/fdm/latest/action/configexport'

# base URI for authentication to get token info
FDMAuth = 'https://' + FDMHost + '/api/fdm/latest/fdm/token'


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


#getting the token info from FDM
response = requests.post(FDMAuth, data=json.dumps(fdm_password_grant), headers=headers, verify=False)
responseJSON = json.loads(bytes.decode(response.content))

#adding token to the header
headers['Authorization'] = 'Bearer ' + responseJSON['access_token']


exportBody = {
 'doNotEncrypt': True,
 'configExportType': 'FULL_EXPORT',
 'deployedObjectsonly': True,
 'type': 'scheduleconfigexport'
}


# atn, verify False, needs cert check
response = requests.post(FDMExport, json.dumps(exportBody), headers=headers, verify=False)


 
