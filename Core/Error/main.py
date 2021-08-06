from Core.ConsoleStyle.style import *

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