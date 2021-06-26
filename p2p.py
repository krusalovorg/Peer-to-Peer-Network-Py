# Импортируем нужные библеотеки
import socket # Импортируем библеотеку socket для работы с сокетами

import _thread # Импортируем библеотеку _thread для работы с потоками

import json # Импортирую библеотеку json для работы с json

# Код

# Классы

ip = []

node = '127.0.0.1', 3030 # Данные об узле

class Server(object):
    def user(self):
        print("Start threard")
        while True:
            try:
                self.data, self.addr = self.sock.recvfrom(1024)  # Читаем сообщения по 1024 байта
                print(self.data)
                if not self.data:
                    break
                if self.data == b'stop':
                    self.conn.close()
            except ConnectionResetError as e:
                self.addr.close()  # Закрываем соеденение

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет

        self.sock.bind(('', 3032))  # Выделяем ip адрес и порт для узла соеденений
        print("P2P Server Started!")
        while True:
            try: self.data, self.addr = self.sock.recvfrom(1024) # Принимаем подключение
            except socket.error:
                pass
            print("Connect:", self.addr)

            user_thread = _thread.start_new_thread(self.user, ())

class Client(object):
    def __init__(self, ip='138.124.186.33'):

        # Инициализация сокета

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет

        self.sock.bind(('', 0)) # Задаем сокет как клиент

        self.sock.sendto('hello, world'.encode(),node) # Отправление тестового сообщения

        self.data, self.addr = self.sock.recvfrom(1024)

        self.data = json.loads(self.data.decode())

        print(self.data)
        if self.data["ip"] == "ip.0":
            if self.data["ip"] == 'null':
                Server()
            else:
                self.__init__(ip=self.data)
        else:
            print("Ваш ip адрес уже зарегестрирован в p2p.network!")

if __name__ == '__main__':
    Client()