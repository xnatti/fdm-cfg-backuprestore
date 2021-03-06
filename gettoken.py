#!/usr/bin/env python3
#
# This snippet just authenticates to the FDM device and prints out the auth token.
# 
# Main purpose is for when you just need the token to use in a cURL workaround
# or for other reasons just need a token for a quick test.
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


print('Firepower Host(IP): ', end='')
FDMHost = input()

print('Username: ', end='')
username = input()

# getpass prints "Password:" on it's own
password = getpass()


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
 return responseJSON['access_token']

print('\n')
print('The authentication token is:')
print(newToken())
print('\n')
