#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/25 10:20
File:main
Author:liuyang97
'''

from .auth import authentication
from .loggers import logger_log
from.ATM_operation import with_draw
from .ATM_operation import transfer
from .ATM_operation import pay_back
from .ATM_operation import view_account_info
from .shopping import shoppings
from .admin import admin_load
from .db_handler import load_account
from .db_handler import save_db

access_logger = logger_log('access')
transaction_logger = logger_log('transaction')


info = [
        ('查看账户信息',view_account_info),
        ('转账',transfer),
        ('还款',pay_back),
        ('取现',with_draw),
        ('购物商城',shoppings),
        ('后台管理',admin_load)
    ]

def conroller(use_boj):
    '功能分发器'
    while True:
        for i,v in enumerate(info):
            print(i,v[0])
        choice = input('请输入您的选择：').strip()
        if not choice:continue
        if choice.isdigit():
            choice = int(choice)
            if choice < len(info) and choice >= 0:
                info[choice][1](use_boj,transaction_logger=transaction_logger,access_logger=access_logger)
def entrance():
    '程序入口'
    user_obj = {
        'is_authentication':False,
        'data':None
    }
    retry_count = 0
    while user_obj['is_authentication'] is not True:
        account = input('请输入账号：').strip()
        password = input('请输入密码：').strip()
        auth_data = authentication(account,password)
        if  auth_data:
            user_obj['is_authentication'] = True
            user_obj['data'] = auth_data
            print('欢迎登陆'.center(50,'*'))
            access_logger.info('%s已登陆'%user_obj['data']['id'])
            conroller(user_obj)
        else:
            print('账号密码错误！')
        retry_count += 1
        if retry_count == 3:
            msg = '用户%s已登陆3失败'%account
            access_logger.error(msg)

            break
