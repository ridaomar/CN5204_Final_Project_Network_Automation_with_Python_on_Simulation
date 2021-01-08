from netmiko import ConnectHandler


def auto_config(device_info, commands):

    device = {
        'device_type': device_info['device_type'],
        'host': device_info['host'],
        'username': device_info['username'],
        'password': device_info['password'],
    }

    try:
        connection = ConnectHandler(**device)
    except Exception as e:
        print(e)

    print("\nEXECUTING COMMANDS...")
    print(connection.send_config_set(commands))

    print("\033[32m✅ Finished!" + "\033[0m")