# Импортируем нужные библеотеки
import socket

from Core.Client.client import *

from Core.Command.cmd import *

from Core.ConsoleStyle.style import *

from Core.Network.net import *

from msvcrt import getch

from node import *

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

os.system('cls' if os.name == 'nt' else 'clear')

print("\n" * 10)
net = Net()
if LOCAL:
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
            net.parse_net()
    except FileNotFoundError:
        console.log(colors.YELLOW,"Config not found!")
        net.parse_net()

    if node_ip == '':
        console.log(colors.WARNING,"Tracker Node not found, start node")
        Start_Node()
else:
    console.log(colors.WARNING,"GLOBAL NETWORK NOT FOUND!")
if __name__ == '__main__':
    if LOCAL:
        cmd()
        console.log(f"{colors.GREEN}Connect to: ",node_ip,colors.ENDC)
        cl = Client(ip=node_ip)