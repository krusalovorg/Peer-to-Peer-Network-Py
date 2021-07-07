# Импортируем нужные библеотеки

import time

import _thread

# Код

# Классы

class cmd(object):
    def _cmd(self):
        while True:
            __cmd = input("> ")
            if __cmd == "stop":
                print("stopppp")
                exit(0)
    def __init__(self):
        _thread.start_new_thread(self._cmd, ())