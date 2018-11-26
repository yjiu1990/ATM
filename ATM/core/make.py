#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/25 21:16
File:make_transfer
Author:liuyang97
'''
from config import setting
from .db_handler import save_db
from .db_handler import load_account


def make_transfer(logger,user_obj,trans_type,amount,**kwargs):
    '交易中心，进行账户间的加减'
    amount = float(amount)
    if trans_type in setting.TRANSACTION_TYPE:
        interest = amount * setting.TRANSACTION_TYPE[trans_type]['interest']
        old_balance = user_obj['data']['balance']
        if setting.TRANSACTION_TYPE[trans_type]['action'] == 'transfer':
            re_account = load_account(kwargs.get('receiving_account'))
            re_account_data = re_account['data']['balance']
            re_account_data_balance = amount + re_account_data + interest
            re_account_data_balance = round(re_account_data_balance, 2)
            new_balance = old_balance - amount - interest
            new_balance = round(new_balance, 2)
            re_account['data']['balance'] = re_account_data_balance
            user_obj['data']['balance'] = new_balance
            save_db(re_account['data'])
            save_db(user_obj['data'])
        elif setting.TRANSACTION_TYPE[trans_type]['action'] == 'plus':
            new_balance = amount + old_balance + interest
            new_balance = round(new_balance,2)
        elif setting.TRANSACTION_TYPE[trans_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            new_balance = round(new_balance, 2)
            if new_balance < 0:
                print('对不起，您的信用额度%s对当前的交易是不够的-%s，你当前的信用额度是%s元'%(user_obj['credit'],(amount+interest)
                                                            ,old_balance))
                return {'status':-1,'error':'交易失败，余额不足'}
        user_obj['data']['balance'] = new_balance
        save_db(user_obj['data'])

        logger.info('account:%s action:%s amount:%s interest:%s balance:%s'%
                    (user_obj['data']['id'],trans_type,amount,interest,new_balance))
        return {'status':0,'msg':'交易成功'}
    else:
        print('对不起，%s交易类型不支持'%trans_type)
        return {'status':1,'error':'交易失败，不支持的类型%s'%trans_type}




