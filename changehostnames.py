# Script that changes the names of meraki devices 

"""The purpose of this script is to change part of the devices name for 
multiple devices. In this case there are multiple devices named 
"site-AccessPoint-1", "site-AccessPoint-2", etc. This script will change them to
"site-AP-1","site-AP-2, etc"""

# import the meraki api python library
from meraki import meraki
import os

# API key and ORG id exported for dev purposes
apikey = os.environ.get('APIKEY')
networkid = os.environ.get('NETWORKID')


# get device info and put it into a list of dictonaries
devices = meraki.getnetworkdevices(apikey, networkid)

oldName = "AccessPoint"
newName = "AP"

# identify the devices with the name to change and change it to the new name

for device in devices:
    if oldName in device['name']:
        device['name'] = device['name'].replace(oldName, newName)
        meraki.updatedevice(apikey, networkid, device['serial'],
         device['name'])
