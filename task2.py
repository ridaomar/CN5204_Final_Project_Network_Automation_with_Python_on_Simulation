from ping3 import ping
import json
import custom_libs.cisco_lib as cisco_lib
import custom_libs.mikrotik_lib as mikrotik_lib

with open('configuration/configuration.json') as sys_config_file:
    sys_config = json.load(sys_config_file)

for device in sys_config['devices']:
    print("\n" + "-" * 35)
    device_ip = device['host']

    if ping(device_ip) is None or False:
        print('\n\033[91m❎ ' + device_ip + ' is off!\033[0m')
        continue
    else:
        print('\n\033[32m✅ ' + device_ip + ' is on!\033[0m')
        print('Vendor: ' + device['device_type'].split('_')[0].upper())
        print('OS: ' + device['device_type'].split('_')[1].upper())

        for device_commands in sys_config['commands']:
            if device['device_type'] == device_commands['type']:
                if device['device_type'] == 'cisco_ios':
                    cisco_lib.auto_config(device, device_commands['commands'])
                elif device['device_type'] == 'mikrotik_routeros':
                    mikrotik_lib.auto_config(device, device_commands['commands'])
                else:
                    print('\033[91m❎ There are no predefined commands to deal with this device!\033[0m')
