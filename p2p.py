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
print("\n" * 10)
if LOCAL:
    print(_OTSTUP + "RUN LOCAL NETWORK")
    for i in range(0, 255):
        res = connect("192.168.1." + str(i), 3030)
        if res:
            print("Device found at: ", "192.168.1." + str(i) + ":" + str(3030),"--->   TRUE","["+"-"*int(i/10)+"]",end="\r")
            break
        else:
            print("Not found device at: ", "192.168.1." + str(i) + ":" + str(3030),"["+"-"*int(i/10)+"]",end="\r")
        res = connect("192.168.0." + str(i), 3030)
        if res:
            print("Device found at: ", "192.168.0." + str(i) + ":" + str(3030),"--->   TRUE","["+"-"*int(i/10)+"]",end="\r")
            break
        else:
            print("Not found device at: ", "192.168.0." + str(i) + ":" + str(3030),"["+"-"*int(i/10)+"]",end="\r")
else:
    print(_OTSTUP + "GLOBAL NETWORK NOT WORK!")

input()
if __name__ == '__main__':
    cmd()
    Client()