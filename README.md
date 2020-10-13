# Snippets for backup and restore for FDM managed Cisco Firepower devices

# Why?

The backup&restore methods available via the GUI on the FDM managed devices are limited to import/export within the same version.
It's also a binary file that limits the possibility of editing and/or auditing.
Using the API allows us to download the configuration in a text format and upload again, even modified, and to a device that's not running the exact same patch release.




## Snippets

* fdm-export.py -- Will export the current configuration to a local file (zipped)
* fdm-import.py -- Allows you to upload a configuration to the FDM device
* fdm-list-configs.py -- Lists available/saved configurations on the device
* fdm-load-config.py -- Allows you to load the configuration into a candidate configuration ready for a commit.
  * (Does not commit autmatically!)

## How to use...

All snippets will prompt you for the device IP address along with credentials.

### fdm-export example
> \> python3 fdm-export.py
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




## Future items to consider

* refine the code so it will not crash on failure
* check if credentials were valid before proceeding
* allowing the export script to wait longer or until job is finished.


