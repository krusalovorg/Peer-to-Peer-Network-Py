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