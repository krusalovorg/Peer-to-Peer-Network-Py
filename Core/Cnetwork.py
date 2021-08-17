# Импортируем библеотеки

from Core.Cconfig import * # Библеотека для работы с конфиг файлом

import socket # Сокеты для работы с сетями

import json # Json для работы с json

import time

import requests

import os
# Класс
class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK_WHITE = '\x1b[0;30;47m'
    RED_WHITE = '\x1b[0;31;47m'
    YELLOW_WHITE = '\x1b[0;33;47m'
    GRAY = '\x1b[1;30;40m'
    GRAY2 = '\x1b[2;37;40m'
end_pre = ""
class console:
    otstup_vert = "\n" * 13
    def initialization():
        os.system("")
    def log(*args,indent_len=0,indent=" ",end="",err=False,logTime=True, info=False):
        now = ''
        now = time.strftime("%Y,%m,%d,%H,%M,%S")
        now = now.split(',')
        now = [int(x) for x in now]

        global end_pre

        str_log = ""

        if end == "":
            if end_pre == "\r":
                end_pre = ""
                str_log = "\n" + indent_len*indent + f' [{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}] '
                for i in args:
                    str_log += i
            else:
                if logTime:
                    if err:
                        str_log = indent_len * indent + f' [{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}] ' + '[ERR] '
                    else:
                        str_log = indent_len * indent + f' [{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}] '

                    if info:
                        str_log = indent_len * indent + f' [{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}] ' + f'[{colors.YELLOW}INFO{colors.ENDC}] '
                    else:
                        str_log = indent_len * indent + f' [{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}] '

                    for i in args:
                        str_log += str(i)
                    #print(indent_len*indent,f'[{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}]',*args,colors.ENDC)
                else:
                    if err:
                        str_log = indent_len * indent + ' [ERR] '
                    else:
                        str_log = indent_len * indent
                    if info:
                        str_log = indent_len * indent + f' [{colors.YELLOW}INFO{colors.ENDC}] '
                    else:
                        str_log = indent_len * indent
                    str_log += indent_len * indent
                    for i in args:
                        str_log += i
                    #print(indent_len*indent,*args,colors.ENDC)
        else:
            end_pre = end
            str_log = indent_len*indent + f' [{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}] '
            for i in args:
                str_log += i
            #print(indent_len*indent,f'[{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}]',*args,colors.ENDC,end=end)

        str_log += colors.ENDC

        if end != "":
            print(str_log, end=end)
        else:
            print(str_log)

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
    def initialization():
        #os.system("netsh advfirewall firewall add rule name=”P2P NETWORK” dir==allow protocol=UDP localport=3030")
        pass
    def clear_cache():
        for root, dirs, files in os.walk('./cache'):
            for filename in files:
                os.remove('./cache/'+str(filename))
                console.log(colors.WARNING,f"Remove from \"./cache\" file: {filename}")
    def download():
        if os.path.exists('./cache/p2p.jpg'):
            os.remove('./cache/p2p.jpg')

        start = time.time()
        file_name = 'p2p.jpg'
        try: r = requests.get('https://raw.githubusercontent.com/krusalovorg/Peer-to-Peer-Network-Py/main/Core/Network/p2p.jpg',stream=True, timeout=5)
        except:
            return 0
        size = int(r.headers.get('Content-Length', 0))
        with open('./cache/'+file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        end = time.time()
        duration = end - start
        sp = (((size * 8) / 1024) / 1024) / duration
        return sp
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