# Импортируем нужные библеотеки

import json

import socket # Импортируем библеотеку socket для работы с сокетами

import _thread # Импортируем библеотеку _thread для работы с потоками

from Server.server import *

from Config.main import *

# Переменные по умолчанию

ip = []

node = '', 3030 # Данные об узле

# Классы

class Client(object):
    def p2p_client(self, ip):
        self.p2pc = ip, 3030 # Данные об клиенте p2p для подключения
        # Инициализация сокета

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет

        self.sock.bind(('',3030)) # Задаем сокет как клиент

        self.sock.sendto(json.dumps({'':''}).encode(), self.p2pc)

        self.data, self.addr = self.sock.recvfrom(1024)

        self.data = json.loads(self.data.decode())

        print(self.data)

    def __init__(self, ip=''):
        node = ip, 3030
        # Инициализация сокета
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет

        self.sock.bind(('', 0)) # Задаем сокет как клиент

        self.sock.sendto(json.dumps({'get': 'ip'}).encode(), node) # Запрашиваем айпи адреса клиентов сети
        self.data, self.addr = self.sock.recvfrom(1024)

        self.data = json.loads(self.data.decode())

        err = self.data["err"]
        if err == "ip.0":
            if self.data["ip"] == 'null':
                p2pserver = _thread.start_new_thread(Server(),())
                self.sock.close()
            else:
                p2pserver = _thread.start_new_thread(Server(),())
                p2pclient = _thread.start_new_thread(self.p2p_client(),(self.data["ip"]))
        elif err == "ip.1":
            print("Ваш ip адрес уже зарегестрирован в p2p.network!")
            self.sock.close()
