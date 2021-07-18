# Импортируем нужные библеотеки

from Core.Client.client import *

from Core.Command.cmd import *

from Core.ConsoleStyle.style import *

from msvcrt import getch

import os

# Глобальные переменные
LOCAL = True
GLOBAL = False
CLOSE = False
_OTSTUP = 10*" "

node_ip = ''

_y = 0
# Код

os.system("")

print("\n" * 10)
print(_OTSTUP + "           ")
print(_OTSTUP + "           ")
print(_OTSTUP + f"Network - {colors.BOLD}LOCAL{colors.ENDC}")
print(_OTSTUP + "          global")
print(_OTSTUP + "          close")

while True:
    key = ord(getch())
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 10)
    if key == 80: # Вверх
        if _y < 2:
            _y += 1
    if key == 72: # Вниз
        if _y > 0:
            _y -= 1
    if key == 13:
        os.system('cls' if os.name == 'nt' else 'clear')
        if CLOSE:
            exit(0)
        break
    if _y == 0:
        print(_OTSTUP + "           ")
        print(_OTSTUP + "           ")
        print(_OTSTUP + f"Network - {colors.BOLD}LOCAL{colors.ENDC}")
        print(_OTSTUP + "          global")
        print(_OTSTUP + "          close")
        LOCAL = True
        GLOBAL = False
        CLOSE = False
    elif _y == 1:
        print(_OTSTUP + "           ")
        print(_OTSTUP + "          local")
        print(_OTSTUP + f"Network - {colors.BOLD}GLOBAL{colors.ENDC}")
        print(_OTSTUP + "          close")
        print(_OTSTUP + "           ")
        LOCAL = False
        GLOBAL = True
        CLOSE = False
    elif _y == 2:
        print(_OTSTUP + "          local")
        print(_OTSTUP + "          global")
        print(_OTSTUP + f"Network - {colors.BOLD}CLOSE{colors.ENDC}")
        print(_OTSTUP + "           ")
        print(_OTSTUP + "           ")
        LOCAL = False
        GLOBAL = False
        CLOSE = True
def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет
    sock.bind(('', 0))  # Задаем сокет как клиент
    sock.settimeout(1)

    node = hostname, port  # Данные об узле

    sock.sendto(json.dumps({'q': 'node?'}).encode(), node)  # Отправление тестового сообщения
    try:
        data, addr = sock.recvfrom(1024)

        data = json.loads(data.decode())

        if data["a"] == "+node":
            result = 1
        if data["a"] == "-node":
            result = 0
        sock.close()
    except socket.error:
        result = 0
    return result

def parse_net():
    if LOCAL:
        print(_OTSTUP + "RUN LOCAL NETWORK")
        for i in range(0, 255):
            res = connect("192.168.1." + str(i), 3030)
            if res:
                print("Tracker Node found at: ", "192.168.1." + str(i) + ":" + str(3030),"--->   TRUE","["+"-"*int(i/10)+"]",end="\r")
                node_ip ='192.168.1.'+str(i)
                config.create_conf(node_ip)
                break
            else:
                print("Not found Tracker Node at: ", "192.168.1." + str(i) + ":" + str(3030),"["+"-"*int(i/10)+"]",end="\r")
            res = connect("192.168.0." + str(i), 3030)
            if res:
                print("Tracker Node found at: ", "192.168.0." + str(i) + ":" + str(3030),"--->   TRUE","["+"-"*int(i/10)+"]",end="\r")
                node_ip ='192.168.0.'+str(i)
                config.create_conf(node_ip)
                break
            else:
                print("Not found Tracker Node at: ", "192.168.0." + str(i) + ":" + str(3030),"["+"-"*int(i/10)+"]",end="\r")
    else:
        print(_OTSTUP + "GLOBAL NETWORK NOT WORK!")

os.system('cls' if os.name == 'nt' else 'clear')

print("\n" * 10)
try:
    config = open('config.conf','r+')
    for line in config:
        console.log(colors.YELLOW,"Load config line: " + line)
        line = line.split("=")
        setting = line[0]
        value = line[1]
        if setting == 'node_ip':
            node_ip = value
    if node_ip == '':
        parse_net()
except FileNotFoundError:
    print("Config not found!")
    parse_net()

print("Connect to Tracker Node")
if __name__ == '__main__':
    if LOCAL:
        cmd()
        print(f"{colors.GREEN}Connect to: ",node_ip,colors.ENDC)
        Client(ip=node_ip)