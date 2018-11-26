#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/24 19:09
File:conf
Author:liuyang97
'''
import  os,sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DB = "%s\db\\accounts"%BASE_DIR


LOG_LEVE = logging.INFO

LOG_TYPE = {
    'access':'access.log',
    'transaction':'transaction.log',
    'shopping':'shopping.log',
    'admin':'admin.log'
}

LOG_FORMATTER =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOG_PATH = os.path.join(BASE_DIR,'log')

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'transfer', 'interest':0.05},
}
