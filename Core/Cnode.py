# Импортируем нужные библеотеки
import json

import socket # Импортируем библеотеку socket для работы с сокетами

import _thread # Импортируем библеотеку _thread для работы с потоками

# Списки

ip = []
SuperNode = []
SuperNodeClients = []

class Node(object):
    threard_num = 0
    def user(self):
        self.threard_num += 1
        print(f"Start threard[{self.threard_num}]")
        while True:
            try:
                try:
                    self.data, self.addr = self.sock.recvfrom(1024)  # Читаем сообщения по 1024 байта
                except socket.error:
                    pass
                print("User", self.addr, "send packet:", self.data)
                if not self.data:
                    break
            except ConnectionResetError as e:
                print("Remove ip addres", self.addr[0], "from db")
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
            print("User", self.addr, "send packet:", self.data)
            self.data = json.loads(self.data.decode())
            if self.data.get("inetspeed"):
                if self.data["inetspeed"] > 5:
                    if SuperNode < 4:
                        print("Send packet {'inetspeed': 'True'} to ", self.addr)
                        self.sock.sendto(json.dumps({'inetspeed': True}).encode(), self.addr)
                    else:
                        print("Send packet {'inetspeed': 'False'} to ", self.addr)
                        self.sock.sendto(json.dumps({'inetspeed': False}).encode(), self.addr)
                else:
                    print("Send packet {'inetspeed': 'False'} to ", self.addr)
                    self.sock.sendto(json.dumps({'inetspeed': False}).encode(), self.addr)

            if self.data.get("add"):
                if self.data["add"] == "ip":
                    if self.addr[0] in ip:
                        print("In ", ip,' include ', self.addr[0])
                        print("Send packet {'add': '-ip'} to ", self.addr)
                        self.sock.sendto(json.dumps({'add': '-ip'}).encode(), self.addr)
                    else:
                        ip.append(self.addr[0])
                        print("Send packet {'add': '+ip'} to ", self.addr)
                        self.sock.sendto(json.dumps({'add': '+ip'}).encode(), self.addr)
                    print(ip)
            if self.data.get("superadd"):
                if self.data["superadd"] == "ip":
                    if self.addr[0] in ip:
                        print("In ", ip,' include ', self.addr[0])
                        print("Send packet {'superadd': '-ip'} to ", self.addr)
                        self.sock.sendto(json.dumps({'superadd': '-ip'}).encode(), self.addr)
                    else:
                        SuperNode.append(self.addr[0])
                        SuperNodeClients.append([])
                        print("Send packet {'superadd': '+ip'} to ", self.addr)
                        self.sock.sendto(json.dumps({'superadd': '+ip'}).encode(), self.addr)
            if self.data.get("q"):
                if self.data["q"] == "node?":
                    print("Send packet {'a': '+node'} to ", self.addr)
                    self.sock.sendto(json.dumps({'a': '+node'}).encode(), self.addr)
            if self.data.get("get"):
                if self.data["get"] == "ip":
                    if len(ip) == 0:
                        print("Send packet {'err': 'ip.0', 'ip': 'null'} to", self.addr)
                        self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': 'null'}).encode(), self.addr)
                    else:
                        if self.addr[0] not in ip:
                            try:
                                if len(SuperNodeClients[0]) < 5:
                                    SuperNodeClients[0].append(self.addr[0])
                                    print("Add ip addres", self.addr[0], "in db")
                                    print("Send packet {'err': 'ip.0', 'ip': " + SuperNode[0] + "} to",
                                              self.addr)
                                    self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': SuperNode[0]}).encode(),
                                                         self.addr)
                                elif len(SuperNodeClients[1]) < 5:
                                    SuperNodeClients[1].append(self.addr[0])
                                    print("Add ip addres", self.addr[0], "in db")
                                    print("Send packet {'err': 'ip.0', 'ip': " + SuperNode[1] + "} to",
                                              self.addr)
                                    self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': SuperNode[1]}).encode(),
                                                         self.addr)
                                elif len(SuperNodeClients[2]) < 5:
                                    SuperNodeClients[2].append(self.addr[0])
                                    print("Add ip addres", self.addr[0], "in db")
                                    print("Send packet {'err': 'ip.0', 'ip': " + SuperNode[2] + "} to",
                                              self.addr)
                                    self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': SuperNode[2]}).encode(),
                                                         self.addr)
                                elif len(SuperNodeClients[3]) < 5:
                                    SuperNodeClients[3].append(self.addr[0])
                                    print("Add ip addres", self.addr[0], "in db")
                                    print("Send packet {'err': 'ip.0', 'ip': " + SuperNode[3] + "} to",
                                              self.addr)
                                    self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': SuperNode[3]}).encode(),
                                                         self.addr)
                                elif len(SuperNodeClients[4]) < 5:
                                    SuperNodeClients[4].append(self.addr[0])
                                    print("Add ip addres", self.addr[0], "in db")
                                    print("Send packet {'err': 'ip.0', 'ip': " + SuperNode[4] + "} to",
                                              self.addr)
                                    self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': SuperNode[4]}).encode(),
                                                         self.addr)
                            except IndexError:
                                print("Send packet {'err': 'ip.0', 'ip': 'null'} to", self.addr)
                                self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': 'null'}).encode(), self.addr)

                            print("Add ip addres", self.addr[0], "in db")
                            print("Send packet {'err': 'ip.0', 'ip': " + SuperNode[len(ip)-1] + "} to", self.addr)
                            self.sock.sendto(json.dumps({'err': 'ip.0', 'ip': ip[len(ip)-1]}).encode(), self.addr)
                        else:
                            print("Send packet {'err': 'ip.1', 'ip': 'err'} to", self.addr)
                            self.sock.sendto(json.dumps({'err': 'ip.1', 'ip': 'err'}).encode(), self.addr)
