# Snippets for backup and restore for FDM managed Cisco Firepower devices

# Why?

The backup&restore methods available via the GUI on the FDM managed devices are limited to import/export within the same version.

It's also a binary file that limits the possibility of editing and/or auditing.

Using the API allows us to download the configuration in a text format and upload again, even modified, and to a device that's not running the exact same patch release.




## Snippets

* [fdm-export.py](fdm-export.py) -- Will export the current configuration to a local file (zipped)
* fdm-import.py -- Allows you to upload a configuration to the FDM device
* fdm-list-configs.py -- Lists available/saved configurations on the device
* fdm-load-config.py -- Allows you to load the configuration into a candidate configuration ready for a commit.
  * (Does not commit autmatically!)

# Installation

Using a virtual environment to run these scripts can be done in the following way:

        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt


## How to use...

All snippets will prompt you for the device IP address along with credentials.

*fdm-export* will only require, and prompt for, IP address and credentials, and will print out the name of the saved file.

*fdm-list-configs* will only require, and prompt for, IP address and credentials, and will print out the available configs. Take note of the diskFileName.

*fdm-import* Requires IP address, credentials and a path to a local filename of the configuration. Usually a .txt file

*fdm-load-config* Requires IP address, credentials and the name of the config as it is displayed in the diskFileName attribute on the FDM device.

*gettoken.py* It's just here to get an authentication token for manual or troubleshooting purposes with cURL

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


### fdm-import example
> \> python3 fdm-import.py 
>
> Firepower Host(IP): 192.168.1.1
>
> Username: admin
>
> Password: 
>
> File name to import: test-upload-config.txt
>
> Response code is: <Response [200]>
>

### fdm-load-config exmaple

> \> python3 load-config.py 
> Firepower Host(IP): 192.168.1.1
>
> Username: admin
>
> Password: 
>
> File name according to FDM (diskFileName): test-upload-config.txt
>
> <Response [200]>
>

### fdm-list-configs example:
>
> \> python3 fdm-list-configs.py 
>
> Firepower Host(IP): 192.168.1.1
>
> Username: admin
>
> Password: 
>
```
{
  "items" : [ {
    "diskFileName" : "test-upload-config.txt",
    "dateModified" : "2020-10-13 11:36:41Z",
    "sizeBytes" : 10931,
    "id" : "default",
    "type" : "configimportexportfileinfo",
    "links" : {
      "self" : "https://192.168.1.1/api/fdm/latest/action/configfiles/default"
    }
  } ],
  "paging" : {
    "prev" : [ ],
    "next" : [ ],
    "limit" : 10,
    "offset" : 0,
    "count" : 10,
    "pages" : 0
  }
}

```

## Future items to consider

* refine the code so it will not crash on failure
* check if credentials were valid before proceeding
* allowing the export script to wait longer or until job is finished.
* Better feedback on the import and load job results.
* Validate use input
