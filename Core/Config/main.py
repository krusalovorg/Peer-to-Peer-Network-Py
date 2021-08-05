# Импортируем библеотеки

from ..ConsoleStyle.style import * # Импортируем функции для работы с консолью

import requests

import json # Импортируем библеотеку для работы с json

# Код

class Config:
    @classmethod
    def get_ip(self):
        try:
            self.config = open('config.conf', 'r+')
            for self.line in self.config:
                self.line = self.line.split("=")
                self.setting = self.line[0]
                self.value = self.line[1]
                if self.setting == 'node_ip':
                    self.node_ip = self.value
                    return str(self.node_ip)
        except FileNotFoundError:
            return ""

    def create_conf(node_ip):
        config = open('config.conf', 'w+')
        config.write("node_ip=" + str(node_ip))
        config.close()
        console.log("\nConfig file create!")

class version:
    @classmethod
    def GetVersion(self):
        try:
            self.version = open('version.json', 'r+')
            self.version = json.load(self.version)
            return self.version['version']
        except FileNotFoundError:
            return ""

    @classmethod
    def CheckVersion(self):
        self.r = requests.get('https://raw.githubusercontent.com/krusalovorg/Peer-to-Peer-Network-Py/main/version.json')
        print(self.r.text[:100])
        self.r = json.load(str(self.r.text[:100]))
        return self.r['version']