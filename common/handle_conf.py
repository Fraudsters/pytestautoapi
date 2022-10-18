import os
from configparser import  ConfigParser
from common.handle_path import CONF_DIR
class Config(ConfigParser):
    def __init__(self,file_name):
        super().__init__()
        self.read(file_name,encoding='utf-8')
conf=Config(os.path.join(CONF_DIR,"config.ini"))

