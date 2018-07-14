# Script that outputs the port config to a text file for all switches
# in a network.

from meraki import meraki
import os

# API key and ORG id exported for dev purposes
apikey = os.environ.get('APIKEY')
networkid = os.environ.get('NETWORKID')

#Get all devices on a network

devices = meraki.getnetworkdevices(apikey, networkid)

# Break out the switches
switches = []
for device in devices:
    if 'MS' in device['model']:
        switches.append(device)

# Write the results to a file
file = open('ports.txt', 'w')

for switch in switches:
    ports = meraki.getswitchports(apikey, switch['serial'])
    file.write("%s\n" % switch['name'])
    for port in ports:
        file.write("%s\n" % port)
 