
import re

#display heading
print('')
print('Devices and their management  IP addresses')
print('________________________________________________')

#create regular expressions to find the mgmt IP address
ip_addr_pattern = re.compile(r'Mgmt:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

#read all lines of dev info form devices-06.txt
file = open('devices-06.txt', 'r')
for line in file:
    #pet dev info into list
    device_info_list = line.strip().split(',')
    #put dev info into dictionaryn for device
    device_info = {} #creating inner dictionary
    device_info['name'] = device_info_list[0]
    #find the Mgmt IP address from the line in the file and put it into device_info
    mgmt_addr = ip_addr_pattern.search(line)
    device_info['ip'] = mgmt_addr.group(1)
    #display device and management IP address
    print(' Device:', device_info['name'], ' Mgmt IP:', device_info['ip'])

print('')
file.close()