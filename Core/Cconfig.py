# Импортируем библеотеки

import requests

import json # Импортируем библеотеку для работы с json

# Код
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

class Config:
    @classmethod
    def get_ip(self):
        try:
            self.config = open('config.conf', 'r+')
            for self.line in self.config:
                self.line = self.line.split("=")
                self.setting = self.line[0]
                self.value = self.line[1]
                if self.setting == 'node_ip':
                    self.node_ip = self.value
                    return str(self.node_ip)
        except FileNotFoundError:
            return ""

    def create_conf(node_ip):
        config = open('config.conf', 'w+')
        config.write("node_ip=" + str(node_ip))
        config.close()
        console.log("Config file create!")

class version:
    @classmethod
    def GetVersion(self):
        try:
            self.version = open('version.json', 'r+')
            self.version = json.load(self.version)
            return self.version['version']
        except FileNotFoundError:
            return ""

    @classmethod
    def CheckVersion(self):
        self.r = requests.get('https://raw.githubusercontent.com/krusalovorg/Peer-to-Peer-Network-Py/main/version.json')
        self.v = str(self.r.text)
        self.v = json.loads(self.v)
        return self.v['version']