from netmiko import ConnectHandler
import threading
import time
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def get_cpu_utilization():
    start = 0;
    end = input("Enter the number of time slots: ")

    device = {
        'device_type': 'cisco_ios',
        'host': '10.10.10.1',
        'username': 'admin',
        'password': 'admin',
        'secret': 'admin'
    }

    try:
        connection = ConnectHandler(**device)
        print("Connected...\n")
    except Exception as e:
        print(e)

    # figure = plt.figure()
    # x = figure.add_subplot(1, 1, 1)
    starting_time = time.time()

    for start in range(int(end)):
        response = connection.send_command('show processes cpu sorted | include CPU utilization')
        cpu_usage = (re.findall(r"[^a-zA-Z]((\d+)((\u0025)|(percent)))[^a-zA-Z0-9]", response))
        cpu_usage = cpu_usage[0][0].replace('%', '')
        print(cpu_usage + '%')
        time_now = time.time()

        text_file = open("temp\\cpu_utilization_temp_file.txt", "a")
        text_file.write(str(time_now - starting_time))
        text_file.write("," + cpu_usage + "\n")
        time.sleep(1)


figure = plt.figure()
xi = figure.add_subplot(1, 1, 1)


def animate_plot(i):
    graph_data = open('temp\\cpu_utilization_temp_file.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    xi.clear()
    xi.plot(xs, ys)


with open("temp\\cpu_utilization_temp_file.txt", "w"):
    pass
cron_job = threading.Thread(target=get_cpu_utilization, name="background")
cron_job.start()
ani = animation.FuncAnimation(figure, animate_plot, interval=1)
plt.show()
