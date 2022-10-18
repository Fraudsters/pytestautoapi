# 用于日志收集
import logging
import os

from common.handle_conf import conf
from common.handle_path import LOG_DIR


def create_log(name="mylog", level="DEBUG", sh_level="DEBUG", file_name="log.log", fh_level="DEBUG"):
    # 创建日志收集器
    log = logging.getLogger(name)
    # 设置日志收集器收集日志级别
    log.setLevel(level)

    # 设置日志收集渠道

    # 1、设置控制台日志输出
    sh = logging.StreamHandler()
    # 2、设置控制台日志输出级别
    sh.setLevel(sh_level)
    log.addHandler(sh)
    # 1、设置文件输出日志
    fh = logging.FileHandler(file_name, encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)

    # 设置日志输出格式
    formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    log_format = logging.Formatter(formats)
    # 绑定日志输出格式
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    return log


my_log=create_log(
    name=conf.get("logging","name"),
    level=conf.get("logging","level"),
    sh_level=conf.get("logging","sh_level"),
    file_name=os.path.join(LOG_DIR,conf.get("logging","file_name")),
    fh_level=conf.get("logging","fh_level")

)
