# Импортируем нужные библеотеки

import _thread

from Core.node import *

# Код

# Классы

class cmd_n:
    def _cmd(self):
        while True:
            __cmd = input("> ")
            if __cmd == "stop":
                exit(0)
            elif __cmd == "clear":
                print("Clearing the IP address database completed successfully!")
            elif __cmd == "list":
                print("IP:",ip)
    def __init__(self):
        _thread.start_new_thread(self._cmd, ())
class cmd(object):
    def _cmd(self):
        while True:
            __cmd = input("> ")
            if __cmd == "stop":
                exit(0)
    def __init__(self):
        _thread.start_new_thread(self._cmd, ())