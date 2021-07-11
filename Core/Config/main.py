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
                    return self.node_ip
        except FileNotFoundError:
            a = 1

    def create_conf(node_ip:str):
        config = open('config.conf', 'w+')
        config.write("node_ip=" + node_ip)
        config.close()
        print("\nConfig file create!")