from netmiko import ConnectHandler


def auto_config(device_info, commands):

    device = {
        'device_type': device_info['device_type'],
        'host': device_info['host'],
        'username': device_info['username'],
        'password': device_info['password'],
        'secret': device_info['enable_password']
    }

    try:
        connection = ConnectHandler(**device)
    except Exception as e:
        print(e)

    try:
        connection.enable()
        print("\n\033[32m✅ Entered to privilege mode!" + "\033[0m")
    except Exception as e:
        print(e)

    try:
        connection.send_command_timing('config t')
        print("\n\033[32m✅ Entered to Configuration mode!" + "\033[0m")
    except Exception as e:
        print(e)

    print("\nEXECUTING COMMANDS...")
    print(connection.send_config_set(commands))
    print()
    print("\033[32m✅ Finished!" + "\033[0m")