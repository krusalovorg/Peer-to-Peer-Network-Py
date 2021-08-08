# Импортируем нужные библеотеки

import threading # Импортируем библеотеку _thread для работы с потоками

from Core.Server.main import *

from Core.Error.main import *

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

        self.sock.bind(('',3031)) # Задаем сокет как клиент

        self.sock.sendto(json.dumps({'test':'test'}).encode(), self.p2pc)

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

            self.sock.settimeout(3) # Максимальное ожидание ответа трекера узлов

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
                        ThreadServer = threading.Thread(target=Server())
                        ThreadServer.start()
                    else:
                        self.sock.close()
                        console.log("ip not null")
                        console.log("Create Peer to Peer Server")
                        ThreadServer = threading.Thread(target=Server())
                        console.log("Connect to Peer to Peer client")
                        ThreadClient = threading.Thread(target=self.p2p_client(self.data["ip"]))
                        ThreadServer.start()
                        ThreadClient.start()
                        #_thread.start_new_thread(self.p2p_client(self.data["ip"]))
                elif err == "ip.1":
                    raise p2p.ip1()
                    self.sock.close()
        except socket.timeout: # Ошибка ip.2 - время ожидание трекера узла вышло
            raise p2p.ip2()
        except socket.gaierror:
            raise p2p.ip3() # Ошибка ip.3 - не корректный ip адрес
        except WindowsError as e: # Ошибка ip.3 - не корректный ip адрес
            if e.winerror == 10013:
                raise p2p.ip3()