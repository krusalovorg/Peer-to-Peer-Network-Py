# Импортируем нужные библеотеки

from Core.Client.client import * # Импортируем функции для работы с клиентом пирининговой сети

from Core.Command.cmd import * # Импортируем функции для работы с входными данными из консоли

from Core.ConsoleStyle.style import * # Импортируем функции для работы с стилями в консоли

from Core.Network.net import * # Импортируем функции для работы с сетями

from node import * # Импортируем функции для запуска трекера узлов

from Core.Config.main import * # Импортируем функции для работы с конфиг файлом

# Код

# Проверка версии клиента децентрализованной сети

console.initialization() # Инициализируем стили в консоли

vers = version

AppVersion = vers.GetVersion()

OfficialVersion = vers.CheckVersion()

if AppVersion == OfficialVersion:
   console.log(colors.BOLD,f"Version: {AppVersion}", logTime=True, info=True)
   console.log(Net.download())
   input()
else:
    console.log(colors.WARNING, f"Your version: {AppVersion}", logTime=True, info=True)
    console.log(colors.WARNING, f"Official Version: {AppVersion}", logTime=True, info=True)
    console.log(colors.BOLD, f"Update [] 0/10", info=True)

# Инициализация меню

network = console.menu() # Запрашиваем у пользователя тип децентрализованной сети

net = Net() # Вызываем класс Net для работы с сетями

node_ip = '' # Создаем переменную для хранения айпи адреса трекера узлов

# Выполнение выбранной команды пользователем

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