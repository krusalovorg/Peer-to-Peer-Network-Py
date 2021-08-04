# Импортируем нужные библеотеки

import time # Импортируем библетеку time

import os

from msvcrt import getch

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
end_pre = ""
class console:
    def initialization():
        os.system("")
    def log(*args,indent_len=0,indent=" ",end="",logTime=True):
        now = ''
        now = time.strftime("%Y,%m,%d,%H,%M,%S")
        now = now.split(',')
        now = [int(x) for x in now]
        global end_pre
        if end == "":
            if end_pre == "\r":
                end_pre = ""
                print("\n",indent_len*indent,f'[{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}]',*args,colors.ENDC)
            else:
                if logTime:
                    print(indent_len*indent,f'[{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}]',*args,colors.ENDC)
                else:
                    print(indent_len*indent,*args,colors.ENDC)
        else:
            end_pre = end
            print(indent_len*indent,f'[{now[0]}-{now[1]}-{now[2]}-{now[3]}-{now[4]}]',*args,colors.ENDC,end=end)

    def menu():
        _OTSTUP = 10 * " "
        print("\n" * 10)
        print(_OTSTUP + "           ")
        print(_OTSTUP + "           ")
        print(_OTSTUP + f"Network - {colors.BOLD}LOCAL{colors.ENDC}")
        print(_OTSTUP + "          global")
        print(_OTSTUP + "          close")

        _y = 0
        select = 0
        while True:
            key = ord(getch())
            if key == 80:  # Вверх
                os.system('cls' if os.name == 'nt' else 'clear')
                if _y < 2:
                    _y += 1
            if key == 72:  # Вниз
                os.system('cls' if os.name == 'nt' else 'clear')
                if _y > 0:
                    _y -= 1
            if key == 13: # Enter
                os.system('cls' if os.name == 'nt' else 'clear')
                if select == 2:
                    exit(0)
                break
            print("\n" * 10)
            if _y == 0:
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                print(_OTSTUP + f"Network - {colors.BOLD}LOCAL{colors.ENDC}")
                print(_OTSTUP + "          global")
                print(_OTSTUP + "          close")
                select = 0
            elif _y == 1:
                print(_OTSTUP + "           ")
                print(_OTSTUP + "          local")
                print(_OTSTUP + f"Network - {colors.BOLD}GLOBAL{colors.ENDC}")
                print(_OTSTUP + "          close")
                print(_OTSTUP + "           ")
                select = 1
            elif _y == 2:
                print(_OTSTUP + "          local")
                print(_OTSTUP + "          global")
                print(_OTSTUP + f"Network - {colors.BOLD}CLOSE{colors.ENDC}")
                print(_OTSTUP + "           ")
                print(_OTSTUP + "           ")
                select = 2
        os.system('cls' if os.name == 'nt' else 'clear')
        return select

    def loading(sec):
        t_end = time.time() + sec
        load = 0
        while time.time() < t_end:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(load)
            if load == 0:
                console.log("-----    ",logTime=False)
                console.log("|        ",logTime=False)
                console.log("|        ",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 1:
                console.log("-------   ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("----------",logTime=False)
            if load == 2:
                console.log("--------  ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("--------- ",logTime=False)
            if load == 3:
                console.log("--------- ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("--------  ",logTime=False)
            if load == 4:
                console.log("----------",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("-------   ",logTime=False)
            if load == 5:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|         ",logTime=False)
                console.log("|         ",logTime=False)
                console.log("------    ",logTime=False)
            if load == 6:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|         ",logTime=False)
                console.log("-----     ",logTime=False)
            if load == 7:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----      ",logTime=False)
            if load == 8:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----     |",logTime=False)
            if load == 9:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----     -",logTime=False)
            if load == 10:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----    --",logTime=False)
            if load == 11:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----   ---",logTime=False)
            if load == 12:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("---- -----",logTime=False)
            if load == 13:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 14 or load == 15:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 16:
                console.log("----------",logTime=False)
                console.log("|        |",logTime=False)
                console.log("         |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 17:
                console.log("----------",logTime=False)
                console.log("         |",logTime=False)
                console.log("         |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 18:
                console.log(" ---------",logTime=False)
                console.log("         |",logTime=False)
                console.log("         |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 19:
                console.log("  --------",logTime=False)
                console.log("         |",logTime=False)
                console.log("         |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 20:
                console.log("   -------",logTime=False)
                console.log("         |",logTime=False)
                console.log("         |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 21:
                console.log("    ------",logTime=False)
                console.log("         |",logTime=False)
                console.log("         |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 22:
                console.log("     -----",logTime=False)
                console.log("         |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("|        |",logTime=False)
                console.log("----------",logTime=False)
            if load == 22:
                load = 0
            else:
                load += 1
            time.sleep(0.05)
            os.system('cls' if os.name == 'nt' else 'clear')