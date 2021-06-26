# Импортируем нужные библеотеки
import json
import socket # Импортируем библеотеку socket для работы с сокетами

import _thread # Импортируем библетеку _thread для работы с потоками

import random

# Код

# Списки

ip = []

# Работа с клиентом
class Node(object):
    def user(self):
        print("Start threard")
        while True:
            try:
                try: self.data, self.addr = self.sock.recvfrom(1024)  # Читаем сообщения по 1024 байта
                except socket.error:
                    pass
                print(self.data)
                if not self.data:
                    break
                if self.data == b'stop':
                    self.addr.close()
            except ConnectionResetError as e:
                ip.remove(self.addr[0])
                self.addr.close() # Закрываем соеденение
                print(f'Cient {self.addr} disconect')

    def __init__(self):
        # Инициализация сокета

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет

        self.sock.bind(('', 3030))  # Выделяем ip адрес и порт для узла соеденений
        while 1:
            try: self.data, self.addr = self.sock.recvfrom(1024)  # Принимаем подключение
            except socket.error:
                pass

            print("Connect:", self.addr)

            if len(ip) == 0:
                self.sock.sendto(json.dumps({'err':'ip.1','ip':'null'}).encode(), self.addr)
                if self.addr not in ip:
                    ip.append(self.addr[0])
                print(ip)
            else:
                if self.addr not in ip:
                    self.sock.sendto(json.dumps({'err':'ip.0','ip':ip[len(ip)]}).encode(), self.addr)
                    ip.append(self.addr[0])
                else:
                    self.sock.sendto(json.dumps({'err':'ip.1','ip':'err'}).encode(), self.addr)

            user_thread = _thread.start_new_thread(self.user,())

if __name__ == "__main__":
    node = Node()