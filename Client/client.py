# Импортируем нужные библеотеки

import json

import socket # Импортируем библеотеку socket для работы с сокетами

import _thread # Импортируем библеотеку _thread для работы с потоками

from Server.server import *

# Переменные по умолчанию

ip = []

node = '127.0.0.1', 3030 # Данные об узле

# Классы

class Client(object):
    def __init__(self, ip='138.124.186.33'):

        # Инициализация сокета

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет

        self.sock.bind(('', 0)) # Задаем сокет как клиент

        self.sock.sendto('hello, world'.encode(),node) # Отправление тестового сообщения

        self.data, self.addr = self.sock.recvfrom(1024)

        self.data = json.loads(self.data.decode())

        print(f"Send {self.addr[0]}:",self.data)
        err = self.data["ip"]
        if err == "ip.0":
            if self.data["ip"] == 'null':
                Server()
            else:
                Server()
                self.__init__(ip=self.data)
        elif err == "ip.1":
            print("Ваш ip адрес уже зарегестрирован в p2p.network!")
