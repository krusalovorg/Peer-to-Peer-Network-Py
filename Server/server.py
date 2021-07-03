# Импортируем нужные библеотеки
import socket # Импортируем библеотеку socket для работы с сокетами

import _thread # Импортируем библеотеку _thread для работы с потоками

# Классы

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

        self.sock.bind(('', 3031))  # Выделяем ip адрес и порт для узла соеденений
        print("P2P Server Started!")
        while True:
            try: self.data, self.addr = self.sock.recvfrom(1024) # Принимаем подключение
            except socket.error:
                pass
            print("Connect:", self.addr)

            user_thread = _thread.start_new_thread(self.user, ())
