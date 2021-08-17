# Импортируем нужные библеотеки

import threading # Импортируем библеотеку _thread для работы с потоками

from Core.Cserver import *
from Core.Cconsolestyle import *
from Core.Cerror import *

# Переменные по умолчанию

node = '', 3030 # Данные об узле

# Классы
def download():
    if os.path.exists('./cache/p2p.jpg'):
        os.remove('./cache/p2p.jpg')

    start = time.time()
    file_name = 'p2p.jpg'
    try:
        r = requests.get(
            'https://raw.githubusercontent.com/krusalovorg/Peer-to-Peer-Network-Py/main/Core/Network/p2p.jpg',
            stream=True, timeout=5)
    except:
        return 0
    size = int(r.headers.get('Content-Length', 0))
    with open('./cache/' + file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    end = time.time()
    duration = end - start
    sp = (((size * 8) / 1024) / 1024) / duration
    return sp


class Client(object):
    def p2p_client(self, ip):
        self.p2pc = ip, 3030 # Данные об клиенте p2p для подключения
        # Инициализация сокета
        console.log("Connect Super-Node!", ip)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет

        self.sock.bind(('',3031)) # Задаем сокет как клиент

        self.sock.sendto(json.dumps({'info':'new user'}).encode(), self.p2pc)

        self.data, self.addr = self.sock.recvfrom(1024)

        console.log("Super-Node send: ", self.data)

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

            self.sock.sendto(json.dumps({'inetspeed': download()}).encode(), node) # Запрашиваем айпи адреса клиентов сети
            self.data, self.addr = self.sock.recvfrom(1024)

            console.log("NODE SEND:",self.data)

            self.data = json.loads(self.data.decode())
            if self.data.get("inetspeed"):
                if self.data["inetspeed"] == True:
                    console.log("Create Peer to Peer Server")
                    ThreadServer = threading.Thread(target=Server.SuperServer())
                    ThreadServer.start()
                else:
                    self.sock.sendto(json.dumps({'get': 'ip'}).encode(), node)  # Запрашиваем айпи адреса клиентов сети
                    self.data, self.addr = self.sock.recvfrom(1024)
            if self.data.get("err"):
                err = self.data["err"]
                if err == "ip.0":
                    if self.data["ip"] == 'null':
                        self.sock.close()
                        console.log("Create Peer to Peer Server")
                        ThreadServer = threading.Thread(target=Server)
                        ThreadServer.start()
                    else:
                        self.sock.close()
                        console.log("ip not null")
                        console.log("Connect to Peer to Peer client")
                        ThreadClient = threading.Thread(target=self.p2p_client(self.data["ip"]))
                        ThreadClient.start()
                        #_thread.start_new_thread(self.p2p_client(self.data["ip"]))
                elif err == "ip.1":
                    raise p2p.ip1()
                    self.sock.close()
                elif err == "ip.4":
                    raise p2p.ip4()
                    self.sock.close()
        except socket.timeout: # Ошибка ip.2 - время ожидание трекера узла вышло
            raise p2p.ip2()
        except socket.gaierror:
            raise p2p.ip3() # Ошибка ip.3 - не корректный ip адрес
        except WindowsError as e: # Ошибка ip.3 - не корректный ip адрес
            if e.winerror == 10013:
                raise p2p.ip3()