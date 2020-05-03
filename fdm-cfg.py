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


FDMURI = 'https://' + FDMHost + '/api/fdm/latest/action/configexport'

headers = {
 'Accept': 'application/json',
 'Content-Type': 'application/json'
}






exportBody = {
 'doNotEncrypt': True,
 'configExportType': 'FULL_EXPORT',
 'deployedObjectsonly': True,
 'type': 'scheduledconfigexport'
}


# atn, verify False, needs cert check

response = requests.post(FDMURI, headers=headers, verify=False)


 
