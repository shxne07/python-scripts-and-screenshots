#Display heading 
print('')
print('Devices with bad software versions')
print('---------------------------------------')

#set variable for current version comparison used in step 4
current_version = 'Version 5.3.1'

#read all lines of dev info from file decices-06.txt
file = open('devices-06.txt', 'r')
for line in file:
    #put dev info into list
    device_info_list = line.strip().split(',')
#pet dev info into dictionary for one dev
    device_info = {} #create inner dictionary of dev info
    device_info['name'] = device_info_list[0]
    device_info['ip'] = device_info_list[2]
    device_info['Version'] = device_info_list[3]

#if version dont match 'current version' display warning
    if device_info['Version'] != current_version:
        print(' Device:', device_info['name'],'  version:', device_info['Version'])
#display blank
print('')
#close file 
file.close()
