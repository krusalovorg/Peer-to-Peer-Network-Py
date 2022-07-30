# Импортируем нужные библеотеки

from Core.Cclient import * # Импортируем функции для работы с клиентом пирининговой сети

from Core.Ccommand import * # Импортируем функции для работы с входными данными из консоли

from Core.Cnetwork import Net # Импортируем функции для работы с сетями

from node import * # Импортируем функции для запуска трекера узлов

from msvcrt import getch

import sys

from Core.Cconfig import * # Импортируем функции для работы с конфиг файлом

from Core.Cerror import *

from Core.Cnode import *

from Core.Cserver import *

import time

import os, ctypes

# Код
end_pre = ""


# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
# if is_admin():
#     print("ADMIN")
# else:
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
#                                         __file__, None, 1)
#     exit()

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
    def GetVersion():
        try:
            version = open('version.json', 'r+')
            version = json.load(version)
            return version['version']
        except FileNotFoundError:
            return ""
    speed_dowonload = Net.download()
    ip = requests.get('http://httpbin.org/ip').json()['origin']
    def Header_menu():
        _OTSTUP = 10 * " "
        console.log(_OTSTUP, colors.BOLD, f"----------{colors.YELLOW}INFO{colors.ENDC}----------", logTime=False)
        console.log(_OTSTUP, colors.BOLD, f"{colors.YELLOW}Version{colors.ENDC}: {console.GetVersion()}", logTime=False,
                    indent_len=2)
        console.log(_OTSTUP, colors.BOLD, f"--------{colors.YELLOW}Internet{colors.ENDC}---------", logTime=False)
        console.log(_OTSTUP, colors.BOLD, f"{colors.BLUE}Dowonload{colors.ENDC}: {console.speed_dowonload}", logTime=False,
                    indent_len=2)
        console.log(_OTSTUP, colors.BOLD, f"{colors.BLUE}Ip{colors.ENDC}: {console.ip}", logTime=False,
                    indent_len=2)
        # console.log(_OTSTUP,colors.BOLD, f"{colors.YELLOW}Net{colors.ENDC}: {Net.download('https://xn---35-6cdk1dnenygj.xn--p1ai/img/users/2019/11/4_ons_black_bg_1920x1080.png')}", logTime=False,indent_len=2)
        # console.log(_OTSTUP,colors.BOLD, f"{colors.YELLOW}Y{colors.ENDC}: {_y}", logTime=False,indent_len=2)
        print("\n")
    def settings():
        _y2 = 0
        _OTSTUP = 10 * " "
        select_color = colors.BLACK_WHITE
        select2 = 0
        print(console.otstup_vert)
        console.Header_menu()
        print(_OTSTUP + "           ")
        print(_OTSTUP + f"Setting - {select_color}CLEAR CACHE{colors.ENDC}")
        print(_OTSTUP + "          BACK")
        while True:
            key = ord(getch())
            if key == 80:  # Вверх
                os.system('cls' if os.name == 'nt' else 'clear')
                if _y2 < 1:
                    _y2 += 1
            if key == 72:  # Вниз
                os.system('cls' if os.name == 'nt' else 'clear')
                if _y2 > 0:
                    _y2 -= 1
            if key == 13:
                break
            print(console.otstup_vert)
            console.Header_menu()
            if _y2 == 0:
                print(_OTSTUP + "           ")
                print(_OTSTUP + f"Setting - {select_color}CLEAR CACHE{colors.ENDC}")
                print(_OTSTUP + "          back")
                select2 = 0
            if _y2 == 1:
                print(_OTSTUP + "          clear cache")
                print(_OTSTUP + f"Setting - {select_color}BACK{colors.ENDC}")
                print(_OTSTUP + "           ")
                select2 = 1
        return select2
    def menu():
        os.system('cls' if os.name == 'nt' else 'clear')

        _y = 0
        select = 0
        input_p = ''
        _OTSTUP = 10 * " "
        select_color = colors.BLACK_WHITE

        print(console.otstup_vert)
        console.Header_menu()
        print(_OTSTUP + "           ")
        print(_OTSTUP + "           ")
        print(_OTSTUP + "           ")
        print(_OTSTUP + "           ")
        print(_OTSTUP + f"Network - {select_color}LOCAL{colors.ENDC}")
        print(_OTSTUP + "          global")
        print(_OTSTUP + "          connect to")
        print(_OTSTUP + "          settings")
        print(_OTSTUP + "          close")
        print(_OTSTUP + "          restart")

        while True:
            key = ord(getch())
            if key == 80:  # Вверх
                os.system('cls' if os.name == 'nt' else 'clear')
                if _y < 5:
                    _y += 1
            if key == 72:  # Вниз
                os.system('cls' if os.name == 'nt' else 'clear')
                if _y > 0:
                    _y -= 1
            if key == 13: # Enter
                os.system('cls' if os.name == 'nt' else 'clear')
                if select == 0:
                    break
                if select == 1:
                    break
                if select == 2:
                    print(_OTSTUP + f"Network - {colors.BOLD}CONNECT TO{colors.ENDC} {colors.GRAY}255{colors.ENDC} {colors.GRAY}255{colors.ENDC} {colors.GRAY}255{colors.ENDC} {colors.GRAY}255{colors.ENDC}",end="\r")
                    select = str(input(_OTSTUP + f"Network - {colors.BOLD}CONNECT TO{colors.ENDC} "))
                    break
                if select == 3:
                    break
                if select == 4:
                    exit(0)
                    break
                if select == 5:
                    break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')

            print(console.otstup_vert)
            console.Header_menu()
            if _y == 0:
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + f"Network - {select_color}LOCAL{colors.ENDC}")
                print(_OTSTUP + "          global")
                print(_OTSTUP + "          connect to")
                print(_OTSTUP + "          settings")
                print(_OTSTUP + "          close")
                print(_OTSTUP + "          restart")
                select = 0
            elif _y == 1:
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "          local")
                print(_OTSTUP + f"Network - {select_color}GLOBAL{colors.ENDC}")
                print(_OTSTUP + "          connect to")
                print(_OTSTUP + "          settings")
                print(_OTSTUP + "          close")
                print(_OTSTUP + "          restart")
                print(_OTSTUP + "           ")
                select = 1
            elif _y == 2:
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "          local")
                print(_OTSTUP + "          global")
                #print(_OTSTUP + f"Network - {colors.BOLD}CONNECT TO{colors.ENDC}")
                print(_OTSTUP + f"Network - {select_color}CONNECT TO{colors.ENDC} (ENTER TO CONTINUE)")
                print(_OTSTUP + "          settings")
                print(_OTSTUP + "          close")
                print(_OTSTUP + "          restart")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                select = 2
            elif _y == 3:
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "          local")
                print(_OTSTUP + "          global")
                print(_OTSTUP + "          connect to")
                print(_OTSTUP + f"Network - {colors.RED_WHITE}SETTINGS{colors.ENDC}")
                print(_OTSTUP + "          close")
                print(_OTSTUP + "          restart")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                select = 3
            elif _y == 4:
                print(_OTSTUP + "           ")
                print(_OTSTUP + "          local")
                print(_OTSTUP + "          global")
                print(_OTSTUP + "          connect to")
                print(_OTSTUP + "          settings")
                print(_OTSTUP + f"Network - {colors.RED_WHITE}CLOSE{colors.ENDC}")
                print(_OTSTUP + "          restart")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                select = 4
            elif _y == 5:
                print(_OTSTUP + "          local")
                print(_OTSTUP + "          global")
                print(_OTSTUP + "          connect to")
                print(_OTSTUP + "          settings")
                print(_OTSTUP + "          close")
                print(_OTSTUP + f"Network - {colors.YELLOW_WHITE}REBOOT{colors.ENDC} the programm")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                select = 5

        os.system('cls' if os.name == 'nt' else 'clear')
        return select
# Инициализация меню

network = console.menu() # Запрашиваем у пользователя тип децентрализованной сети

net = Net() # Вызываем класс Net для работы с сетями

Net.initialization() # Инициализация порта

node_ip = '' # Создаем переменную для хранения айпи адреса трекера узлов

# Выполнение выбранной команды пользователем
while True:
    if network == 3: # Выбор меню settings
        select2 = console.settings() # Запуск меню settings
        if select2 == 1: # Выбор в меню BACK
            network = console.menu()  # Запрашиваем у пользователя тип децентрализованной сети
        if select2 == 0: # В
            Net.clear_cache()
            network = console.menu()  # Запрашиваем у пользователя тип децентрализованной сети
    if network != 3:
        break

if network == 0: # Проверка выбрал ли пользователь запуск локальной сети
    node_ip = Config.get_ip() # Получаем айпи адрес трекера узлов из конфиг файла
    if node_ip == "this.node": # Если в конфиг файле указано что это трекер узлов
        console.log(colors.WARNING,"Start tracker node") # Уведомление пользователя о запуске трекера узлов
        Start_Node()  # Запуск трекера узлов
    elif node_ip == "": # Проверка найден ли айпи айдрес
        node_ip = net.parse_net() # Запускаем парсер локальной сети для поиска трекера узлов
        if node_ip == "": # Проверка найден ли айпи айдрес
            console.log(colors.WARNING,"Tracker Node not found, start node") # Уведомление пользователя если не найден айпи адрес трекера узлов
            Config.create_conf("this.node")
            Start_Node() # Запуск трекера узлов
    elif node_ip != "this.node": # Если не найден айпи адрес
        Config.create_conf(node_ip) # Создание конфиг файла и указание найденного айпи адреса
if network == 1: # Если пользователь выбрал запуск/вход в глобальную сеть
    console.log(colors.WARNING,"GLOBAL NETWORK NOT FOUND!") # Уведомелнение пользователя так как не найдена глобальная сеть
    input('Press Enter to close: ') # Уведомление пользователя как закрыть программу
if isinstance(network, str): # Если пользователь выбрал подключение к трекеру узлов по айпи адресу
    node_ip = network # Присваиваем значение айпи адреса трекера узлов к переменной node_ip
if network == 5:
    os.execv(sys.executable, [sys.executable] + sys.argv)
# Блок запуска алгоритов присоеденения к сети

if __name__ == '__main__':
    if network == 0: # Выполнение выбранной команды пользователем (Подключение к локальной сети)
        cmd() # Запуск консоли
        console.log(f"{colors.GREEN}Connect to: ",node_ip,colors.ENDC) # Уведомление пользователя о подключении к трекеру узлов
        cl = Client(ip=node_ip) # Запуск алгоритма подключения к децентрализованной сети
    if isinstance(network, str): # Выполнение выбранной команды пользователем (Подключение к определенному трекеру узлов)
        cmd() # Запуск консоли
        console.log(f"{colors.YELLOW}Connect to: ",node_ip,colors.ENDC) # Уведомление пользователя о подключении к трекеру узлов
        cl = Client(ip=node_ip) # Запуск алгоритма подключения к децентрализованной сети