# Импортируем библеотеки

from ..ConsoleStyle.style import * # Стилизация логов

from ..Config.main import * # Библеотека для работы с конфиг файлом

import socket # Сокеты для работы с сетями

import json # Json для работы с json

# Класс
def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сокет
    sock.bind(('', 0))  # Задаем сокет как клиент
    sock.settimeout(0.1)

    node = hostname, port  # Данные об узле

    sock.sendto(json.dumps({'q': 'node?'}).encode(), node)  # Отправление тестового сообщения
    try:
        data, addr = sock.recvfrom(1024)

        data = json.loads(data.decode())

        if data["a"] == "+node":
            result = 1
        if data["a"] == "-node":
            result = 0
        sock.close()
    except socket.error:
        result = 0
    return result


class Net:
    def download(self, path):
        self.start = time.time()
        self.file_name = '4_ons_black_bg_1920x1080'
        try:
            self.r = requests.get(self.path, stream=True, timeout=5)
        except:
            return 0
        self.size = int(self.r.headers.get('Content-Length', 0))
        with open(self.file_name, 'wb') as self.f:
            for self.chunk in self.r.iter_content(chunk_size=1024):
                if self.chunk:
                    self.f.write(self.chunk)

        self.end = time.time()
        self.duration = self.end - self.start
        self.sp = (((self.size * 8) / 1024) / 1024) / self.duration
        return self.sp

    def upload(self, path):
        self.start = time.time()
        self.file_name = '4_ons_black_bg_1920x1080.png'
        with open(self.file_name, 'rb') as self.f:
            self.files = {'Upload': (self.file_name, self.f.read())}
        try:
            requests.post(self.path, files=self.files)
        except:
            return 0
        self.size = self.os.path.getsize(self.file_name)
        self.end = self.time.time()
        self.duration = self.end - self.start
        self.sp = (((self.size * 8) / 1024) / 1024) / self.duration

        return self.sp

    def parse_net(self):
        console.log(colors.YELLOW,"RUN LOCAL NETWORK")
        node_ip = ""
        for i in range(0, 255):
            self.ip = "192.168.1." + str(i)
            self.res = connect(self.ip, 3030)
            if self.res:
                console.log(colors.GREEN,"Tracker Node found at: ", "192.168.1." + str(i) + ":" + str(3030), "--->   TRUE","[" + "-" * int(i / 10) + "]", end="\r")
                self.node_ip = '192.168.1.' + str(i)
                Config.create_conf(self.node_ip)
                break
            else:
                console.log(colors.YELLOW,"Not found Tracker Node at: ", "192.168.1." + str(i) + ":" + str(3030),
                          "[" + "-" * int(i / 10) + "]", end="\r")
                self.node_ip = ""
                self.res = connect("192.168.0." + str(i), 3030)
                if self.res:
                    console.log(colors.GREEN,"Tracker Node found at: ", "192.168.0." + str(i) + ":" + str(3030), "--->   TRUE","[" + "-" * int(self.i / 10) + "]", end="\r")
                    node_ip = '192.168.0.' + str(i)
                    Config.create_conf(node_ip)
                    break
                else:
                    console.log(colors.YELLOW,"Not found Tracker Node at: ", "192.168.0." + str(i) + ":" + str(3030),
                          "[" + "-" * int(i / 10) + "]", end="\r")
                    self.node_ip = ""
        return self.node_ip