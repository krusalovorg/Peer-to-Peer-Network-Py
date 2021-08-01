# Импортируем нужные библеотеки

import time # Импортируем библетеку time

# Классы

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
global end_pre
class console:
    def log(*args,indent_len=0,indent=" ",end=""):
        now = ''
        now = time.strftime("%Y,%m,%d,%H,%M,%S")
        now = now.split(',')
        now = [int(x) for x in now]
        if end == "":
            if global end_pre == "\r":
                end_pre = ""
                print("\n",indent_len*indent,f'[{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}]',*args,colors.ENDC)
        else:
            end_pre = end
            print(indent_len*indent,f'[{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}]',*args,colors.ENDC,end=end)