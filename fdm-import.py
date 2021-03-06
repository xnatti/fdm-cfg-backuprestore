#!/usr/bin/env python3
# 
# This snippet can be used to upload a file to FDM.
# 
# A part of the code is created based on information found on the following websites regarding multipart uploading and using the prepare() in requests
# https://franklingu.github.io/programming/2017/10/30/post-multipart-form-data-using-requests/
# prepared https://requests.readthedocs.io/en/master/user/advanced/
# Cisco's guide with cURL examples: https://www.cisco.com/c/en/us/td/docs/security/firepower/ftd-api/guide/ftd-rest-api/ftd-api-import-export.html
#
# 

import requests
import json
from getpass import getpass
from requests import Request, Session

# Disable insecure request warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# To load the config via cURL
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

print('\nFirepower Host(IP): ', end='')
FDMHost = input()

print('Username: ', end='')
username = input()

# getpass prints "Password:" on it's own
password = getpass()

print('File name to import: ', end='')
fileName = input()

FDMUploadURI = 'https://' + FDMHost + '/api/fdm/latest/action/uploadconfigfile'

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

# popping the content-type from the header
# because the next request will autopopulate with the correct values

headers.pop('Content-Type')

s = Session()

multipart_req = Request('POST', FDMUploadURI, files={'name': open(fileName, 'r')}, headers = headers).prepare()

response = s.send(multipart_req, verify=False)
print('We are hoping for a HTTP response code of 200')
print('Response code is: ' + str(response))
print('\n\n')
# in order to verify header stuff print(multipart_req.body.decode('utf-8'))


# to list files: response = requests.get('https://FDM/api/fdm/latest/action/configfiles', headers=headers, verify=False)
