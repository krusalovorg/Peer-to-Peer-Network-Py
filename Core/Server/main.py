# Импортируем нужные библеотеки
from Core.Config.main import * # Импортируем библеотеку config для работы с конфиг файлом

import socket # Импортируем библеотеку socket для работы с сокетами

import _thread # Импортируем библеотеку _thread для работы с потоками

import json

from Core.Error.main import *

# Классы
def add_ip():
    # Инициализация сокета
    node = Config.get_ip(), 3030
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет

    sock.bind(('', 0)) # Задаем сокет как клиент

    sock.sendto(json.dumps({'add': 'ip'}).encode(), node) # Запрашиваем айпи адреса клиентов сети
    data, addr = sock.recvfrom(1024)

    data = json.loads(data.decode())
    if data.get("add"):
        sock.close()
        if data["add"] == "+ip":
            console.log(colors.GREEN,"IP address has been successfully added to the database!",colors.ENDC)
            return True
        if data["add"] == "-ip":
            console.log(colors.FAIL,"IP address has not been added to the database!",colors.ENDC)
            return False

class Server:
    def user(self):
        while True:
            try:
                self.data, self.addr = self.sock.recvfrom(1024)  # Читаем сообщения по 1024 байта
                console.log(colors.YELLOW,"User", self.addr, "send packet:", self.data,colors.ENDC)
                if not self.data:
                    break
            except ConnectionResetError as e:
                self.addr.close()  # Закрываем соеденение

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет

        self.sock.bind(('', 3031))  # Выделяем ip адрес и порт для узла соеденений

        console.log(colors.GREEN,"P2P Server Started!",colors.ENDC)

        if add_ip():
            console.log(colors.GREEN,"You join to Peer to Peer Network!",colors.ENDC)
        else:
            console.log(colors.RED,"An unexpected error has occurred!",colors.ENDC)

        while True:
            try: self.data, self.addr = self.sock.recvfrom(1024) # Принимаем подключение
            except socket.error:
                pass
            console.log(colors.CYAN,"Connect:", self.addr,colors.ENDC)
            user_thread = _thread.start_new_thread(self.user, ())
