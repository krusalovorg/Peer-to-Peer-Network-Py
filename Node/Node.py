# Импортируем нужные библеотеки
import json

import socket # Импортируем библеотеку socket для работы с сокетами

import _thread # Импортируем библеотеку _thread для работы с потоками

# Списки

ip = []

class Node(object):
    def user(self):
        print("Start threard")
        while True:
            try:
                try:
                    self.data, self.addr = self.sock.recvfrom(1024)  # Читаем сообщения по 1024 байта
                except socket.error:
                    pass
                print(self.data)
                if not self.data:
                    break
                if self.data == b'stop':
                    self.addr.close()
            except ConnectionResetError as e:
                ip.remove(self.addr[0])
                self.addr.close()  # Закрываем соеденение
                print(f'Cient {self.addr} disconect')

    def __init__(self):
        # Инициализация сокета

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет

        self.sock.bind(('', 3030))  # Выделяем ip адрес и порт для узла соеденений
        while 1:
            try:
                self.data, self.addr = self.sock.recvfrom(1024)  # Принимаем подключение
            except socket.error:
                pass

            print("Connect:", self.addr)

            self.data = json.loads(self.data.decode())

            if self.data["q"] == "node?":
                self.sock.sendto(json.dumps({'a': '+node'}).encode(), self.addr)
            else:
                if len(ip) == 0:
                    self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': 'null'}).encode(), self.addr)
                else:
                    if self.addr not in ip:
                        self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': ip[len(ip)]}).encode(), self.addr)
                    else:
                        self.sock.sendto(json.dumps({'err': 'ip.1', 'ip': 'err'}).encode(), self.addr)
                if self.addr not in ip:
                    ip.append(self.addr[0])
                    print(ip)
                user_thread = _thread.start_new_thread(self.user, ())
