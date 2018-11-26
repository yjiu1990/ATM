#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/25 10:35
File:auth
Author:liuyang97
'''
from .db_handler import load_account

def authentication(account,password):
    '验证账户'
    account_data = load_account(account)
    # print(account_data)
    if account_data['status'] == 0:
        account_data = account_data['data']
        if password == account_data['password']:
            # print(account_data)
            return account_data
        else:
            return None
    else:
        return '账户已被锁定！'
def auth(fun):
    def wrapper(*args,**kwargs):
        if args[0].get('is_authentication'):
            return fun(*args,**kwargs)
        else:
            print('用户不能登陆！')
    return wrapper
