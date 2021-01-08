from ping3 import ping
import json
import custom_libs.cisco_lib as cisco_lib
import custom_libs.mikrotik_lib as mikrotik_lib

# Open configuration file
with open('configuration/configuration.json') as sys_config_file:
    # read the configuration file as dictionary
    sys_config = json.load(sys_config_file)

# Loop over the network devices
for device in sys_config['devices']:
    print("\n" + "-" * 35)
    device_ip = device['host']

    # Ping the device
    if ping(device_ip) is None or False:
        # If the device is disconnected, display an error message and go to the next device
        print('\n\033[91m❎ ' + device_ip + ' is off!\033[0m')
        continue
    else:
        # If the device is connected, display it's information
        print('\n\033[32m✅ ' + device_ip + ' is on!\033[0m')
        print('Vendor: ' + device['device_type'].split('_')[0].upper())
        print('OS: ' + device['device_type'].split('_')[1].upper())

        # Loop over the available commands types
        for device_commands in sys_config['commands']:
            # Check if the device type was already known and the user defined it's commands
            if device['device_type'] == device_commands['type']:
                if device['device_type'] == 'cisco_ios':
                    cisco_lib.auto_config(device, device_commands['commands'])
                elif device['device_type'] == 'mikrotik_routeros':
                    mikrotik_lib.auto_config(device, device_commands['commands'])
                else:
                    # displaying an error message if the device doesn't has a pre defined commands
                    print('\033[91m❎ There are no predefined commands to deal with this device!\033[0m')
