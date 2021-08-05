# Импортируем нужные библеотеки

import _thread # Импортируем библеотеку _thread для работы с потоками

from Core.Server.server import *

import sys
# Переменные по умолчанию

ip = []

node = '', 3030 # Данные об узле

# Классы

class Client(object):
    def p2p_client(self, ip):
        self.p2pc = ip, 3030 # Данные об клиенте p2p для подключения
        # Инициализация сокета
        console.log("CONNECT TO PEER TO PEER CLIENT!!!!!!!!!!!!!!", ip)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет

        self.sock.bind(('',3030)) # Задаем сокет как клиент

        self.sock.sendto(json.dumps({'':''}).encode(), self.p2pc)

        self.data, self.addr = self.sock.recvfrom(1024)

        console.log("P2P SEND: ", self.data)

        self.data = json.loads(self.data.decode())

        console.log(self.data)

    def __init__(self, ip=''):
        node = ip, 3030
        try:
            # Инициализация сокета
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет

            self.sock.bind(('', 0)) # Задаем сокет как клиент

            self.sock.settimeout(0.1) # Максимальное ожидание ответа трекера узлов

            console.log(f"{colors.YELLOW}Request IP address of client p2p",colors.ENDC) # Уведомление пользователя о запрашивания айпи адресов клиентов сети

            self.sock.sendto(json.dumps({'get': 'ip'}).encode(), node) # Запрашиваем айпи адреса клиентов сети
            self.data, self.addr = self.sock.recvfrom(1024)

            console.log("NODE SEND:",self.data)

            self.data = json.loads(self.data.decode())
            if self.data.get("err"):
                err = self.data["err"]
                if err == "ip.0":
                    if self.data["ip"] == 'null':
                        self.sock.close()
                        console.log("Create Peer to Peer Server")
                        _thread.start_new_thread(Server(),())
                    else:
                        self.sock.close()
                        console.log("ip not null")
                        console.log("Create Peer to Peer Server")
                        _thread.start_new_thread(Server(),())
                        console.log("Connect to Peer to Peer client")
                        _thread.start_new_thread(self.p2p_client(self.data["ip"]))
                elif err == "ip.1":
                    console.log("Ваш ip адрес уже зарегестрирован в p2p.network!")
                    self.sock.close()
        except socket.timeout:
            console.log(f"{colors.RED}The node tracker timeout has expired!",colors.ENDC,err=True) # Уведомление пользователя о ошибке (время ожидание трекера узлов вышло)
            console.log(f"{colors.RED}Check your internet connection and local network integrity!",colors.ENDC, err=True) # Уведомление пользователя как можно решить проблему
            input('')
        except socket.gaierror:
            console.log(f"{colors.RED}Wrong IP address of node tracker received!",colors.ENDC,err=True) # Уведомление пользователя о ошибке (не корректный айпи адрес трекера узлов)
            console.log(f"{colors.RED}There are several solutions to this problem:",colors.ENDC,err=True) # Уведомление пользователя как можно решить проблему
            console.log(f"{colors.RED}1. Copy the IP address of the node tracker from the official site of the peer-to-peer network",colors.ENDC,err=True) # Уведомление пользователя как можно решить проблему
            console.log(f"{colors.RED}2. Before connecting to the peer-to-peer network, select the {colors.YELLOW}{colors.BOLD}connect to{colors.ENDC}{colors.RED} connection type in the menu and enter the copied IP address there.",colors.ENDC,err=True) # Уведомление пользователя как можно решить проблему
            input('')