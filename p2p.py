# Импортируем нужные библеотеки
import socket

from Client.client  import *

from Command.cmd  import *

from msvcrt import getch

import os

# Глобальные переменные
LOCAL = True
GLOBAL = False

_OTSTUP = 10*" "

node_ip = ''

# Код

print("\n" * 10)
print(_OTSTUP + "Network - LOCAL")
print(_OTSTUP + "          global")

while True:
    key = ord(getch())
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 10)
    if key == 72:
        print(_OTSTUP + "Network - LOCAL")
        print(_OTSTUP + "          global")
        LOCAL = True
        GLOBAL = False
    if key == 80:
        print(_OTSTUP + "Network - GLOBAL")
        print(_OTSTUP + "          local")
        GLOBAL = True
        LOCAL = False
    if key == 13:
        os.system('cls' if os.name == 'nt' else 'clear')
        break

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

def create_conf(node_ip):
    config = open('config.conf','w+')
    config.write("node_ip="+node_ip)
    config.close()
    print("\nConfig file create!")

def parse_net():
    if LOCAL:
        print(_OTSTUP + "RUN LOCAL NETWORK")
        for i in range(150, 255):
            res = connect("192.168.1." + str(i), 3030)
            if res:
                print("Device found at: ", "192.168.1." + str(i) + ":" + str(3030),"--->   TRUE","["+"-"*int(i/10)+"]",end="\r")
                node_ip ='192.168.1.'+str(i)
                create_conf(node_ip)
                break
            else:
                print("Not found device at: ", "192.168.1." + str(i) + ":" + str(3030),"["+"-"*int(i/10)+"]",end="\r")
            res = connect("192.168.0." + str(i), 3030)
            if res:
                print("Device found at: ", "192.168.0." + str(i) + ":" + str(3030),"--->   TRUE","["+"-"*int(i/10)+"]",end="\r")
                node_ip ='192.168.0.'+str(i)
                create_conf(node_ip)
                break
            else:
                print("Not found device at: ", "192.168.0." + str(i) + ":" + str(3030),"["+"-"*int(i/10)+"]",end="\r")
    else:
        print(_OTSTUP + "GLOBAL NETWORK NOT WORK!")

os.system('cls' if os.name == 'nt' else 'clear')

print("\n" * 10)
try:
    config = open('config.conf','r+')

    for line in config:
        print("Load config line: " + line)
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
    cmd()
    Client(ip=node_ip)