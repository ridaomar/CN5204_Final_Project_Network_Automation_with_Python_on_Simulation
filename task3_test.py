from netmiko import ConnectHandler
import threading
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def check_CPU_Utilization_Live_Gragh():
    router = {'device_type': 'mikrotik_routeros',
              'host': '192.168.10.10',
              'username': 'admin',
              'password': 'admin'}
    conn = ConnectHandler(**router)
    conn.find_prompt()
    program_starts = time.time()

    while True:
        output = conn.send_command_timing("system resourc cpu print detail")
        a = output.split()
        now = time.time()
        cpu_Load = list(a[2])
        print(cpu_Load)

        text_file = open("CPU_Load.txt", "a")
        text_file.write(str(now - program_starts))
        text_file.write(",")
        text_file.write(cpu_Load[5])
        text_file.write("\n")




def animate(i):
    graph_data = open('CPU_Load.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs,ys)

def delet_File_Content(file_Name):
    with open(file_Name, "w"):
        pass


delet_File_Content("CPU_Load.txt")
b = threading.Thread(name='background', target=check_CPU_Utilization_Live_Gragh)
b.start()
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()