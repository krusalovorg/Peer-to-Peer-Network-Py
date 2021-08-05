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

console.log(colors.OKCYAN,f"Version: {AppVersion}")

OfficialVersion = vers.CheckVersion()

if AppVersion == OfficialVersion:
   console.log("You have the official version of the peer-to-peer network client installed!")

input()
# Инициализация меню

network = console.menu() # Запрашиваем у пользователя тип децентрализованной сети

net = Net() # Вызываем класс Net для работы с сетями

node_ip = '' # Создаем переменную для хранения айпи адреса трекера узлов

# Выполнение выбранной команды пользователем

if network == 0: # Проверка выбрал ли пользователь запуск локальной сети
    node_ip = Config.get_ip() # Получаем айпи адрес трекера узлов из конфиг файла
    if node_ip == "": # Проверка найден ли айпи айдрес
        node_ip = net.parse_net() # Запускаем парсер локальной сети для поиска трекера узлов
        if node_ip == "": # Проверка найден ли айпи айдрес
            console.log(colors.WARNING,"Tracker Node not found, start node") # Уведомление пользователя если не найден айпи адрес трекера узлов
            Start_Node() # Запуск трекера узлов
    else: # Если не найден айпи адрес
        Config.create_conf(node_ip) # Создание конфиг файла и указание найденного айпи адреса
if network == 1: # Если пользователь выбрал запуск/вход в глобальную сеть
    console.log(colors.WARNING,"GLOBAL NETWORK NOT FOUND!") # Уведомелнение пользователя так как не найдена глобальная сеть
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