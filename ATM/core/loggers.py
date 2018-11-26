#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/23 9:21
File:logger
Author:liuyang97
'''
from config import setting
import logging
import os
from logging import handlers
def logger_log(log_type):
    log = logging.getLogger(log_type)
    log.setLevel(setting.LOG_LEVE)

    file_log = os.path.join(setting.LOG_PATH,setting.LOG_TYPE[log_type])
    fh = handlers.TimedRotatingFileHandler(file_log,when='D',interval=3,encoding='utf-8')
    log.addHandler(fh)

    file = setting.LOG_FORMATTER
    fh.setFormatter(file)
    return log


