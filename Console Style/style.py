# Импортируем нужные библеотеки

import time # Импортируем библетеку time

class CConsole(object):
    def _print(self,text):
        for i in range(len(text)):
            time.sleep(0.1)
            print(text[i])
