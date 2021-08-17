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

class p2p(Exception):
    def ip0():
        pass
    def ip1():
        console.log(f"[IP.1] {colors.FAIL}This IP address is already registered in the p2p.network!", colors.ENDC,
                    err=True)  # Уведомление пользователя о ошибке (не корректный айпи адрес трекера узлов)
    def ip2():
        console.log(f"[IP.2] {colors.FAIL}Node tracker not responding!", colors.ENDC,
                    err=True)  # Уведомление пользователя о ошибке (не корректный айпи адрес трекера узлов)
        console.log(f"{colors.FAIL}The node tracker timeout has expired!", colors.ENDC,
                    err=True)  # Уведомление пользователя о ошибке (время ожидание трекера узлов вышло)
        console.log(f"{colors.FAIL}Check your internet connection and local network integrity!", colors.ENDC,
                    err=True)  # Уведомление пользователя как можно решить проблему
    def ip3():
        console.log(f"[IP.3] {colors.FAIL}IP address is not correct!", colors.ENDC,
                    err=True)  # Уведомление пользователя о ошибке (не корректный айпи адрес трекера узлов)
        console.log(f"{colors.FAIL}Wrong IP address of node tracker received!", colors.ENDC,
                    err=True)  # Уведомление пользователя о ошибке (не корректный айпи адрес трекера узлов)
        console.log(f"{colors.FAIL}There are several solutions to this problem:", colors.ENDC,
                    err=True)  # Уведомление пользователя как можно решить проблему
        console.log(
            f"{colors.FAIL}1. Copy the IP address of the node tracker from the official site of the peer-to-peer network",
            colors.ENDC, err=True)  # Уведомление пользователя как можно решить проблему
        console.log(
            f"{colors.FAIL}2. Before connecting to the peer-to-peer network, select the {colors.YELLOW}{colors.BOLD}connect to{colors.ENDC}{colors.FAIL} connection type in the menu and enter the copied IP address there.",
            colors.ENDC, err=True)  # Уведомление пользователя как можно решить проблему
    def ip4():
        pass
    def ip5():
        pass
    pass