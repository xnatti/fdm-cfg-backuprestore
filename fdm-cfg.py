#!/usr/bin/env python3

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


exportBody = {
 'doNotEncrypt': True,
 'configExportType': 'FULL_EXPORT',
 'deployedObjectsonly': True,
 'type': 'scheduledconfigexport'
}
