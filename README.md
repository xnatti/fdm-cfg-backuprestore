# Snippets for backup and restore for FDM managed Cisco Firepower devices

## Snippets

* fdm-export.py -- Will export the current configuration to a local file (zipped)
* fdm-import.py -- Allows you to upload a configuration to the FDM device
* fdm-list-configs.py -- Lists available/saved configurations on the device
* fdm-load-config.py -- Allows you to load the configuration into a candidate configuration ready for a commit.
  * (Does not commit autmatically!)

## How to use...

All snippets will prompt you for the device IP address along with credentials.

### fdm-export example
> > python3 fdm-export.py
>
> Firepower Host(IP): 192.168.1.1
>
> Username: admin
>
> Password: 
>
> Waiting 15 sec for job to maybe finish...
>
> Job finished, lets get that file
>
> Download successful
>
> Attempting to write to Exported-at-2020-10-13-12-38-48Z.zip 



Testing using the API to a FirePower (FDM managed) 6.6 device to download and restore config

## Why am I not using (...)

There are a few reasons.

1. I'm practising, and I'm not there yet, knowledge wise.
2. ...

## Stuff to remember

If I modify the objects and impoort into a new device, I should remove version and id attributes.
Future consideration would be a clean-up task.

