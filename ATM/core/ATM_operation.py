#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/24 19:42
File:ATM_operation
Author:liuyang97
'''
from .loggers import logger_log
from .make import make_transfer
from .auth import auth

def view_account_info(account_data,*args,**kwargs):
    '查询账户信息'
    # print(account_data)
    trans_logger = kwargs.get('transaction_logger')
    print('账户个人信息'.center(50,'*'))
    for k,v in account_data['data'].items():
        if k not in ('password'):
            print('%15s:%s'%(k,v))
    print('END'.center(50,'*'))
    trans_logger.info('%s查询了账户信息'%account_data['data']['id'])
@auth
def transfer(account_data,*args,**kwargs):
    '账户转账'
    trans_logger = kwargs.get('transaction_logger')
    print('账户余额'.center(50,'*'))
    print('credit:%s\n'
          'blance:%s'%(account_data['data']['credit'],account_data['data']['balance']))
    flag_exit = False
    while not flag_exit:
        receiving_account = input('请输入接收账号或按B返回：').strip()
        transfer_amount = input('请输入转账金额按B返回：').strip()
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            transfer_amount = int(transfer_amount)
            if (account_data['data']['balance'] / 2) >= transfer_amount:
                transaction_result = make_transfer(trans_logger,account_data,'transfer',transfer_amount,
                                                   receiving_account=receiving_account)
                if transaction_result['status'] == 0:
                    print('成功转账%s元，余额还有%s'%(transfer_amount,account_data['data']['balance']))
                else:
                    print(transaction_result)
            else:
                print('余额不足，可转账%s元'%int(account_data['data']['balance']/2))
        else:
            print('输入错误！')
        if receiving_account == 'b'.lower():
            flag_exit = True
@auth
def with_draw(account_data,*args,**kwargs):
    '取现'
    trans_logger = kwargs.get('transaction_logger')
    print('账户余额'.center(50,'*'))
    print('credit:%s\n'
          'blance:%s'%(account_data['data']['credit'],account_data['data']['balance']))
    flag_exit = False
    while not flag_exit:
        withdraw_amount = input('请输入提现的金额或按按B返回：').strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
            if (account_data['data']['balance'] / 2) >= withdraw_amount:
                transaction_result = make_transfer(trans_logger,account_data,'withdraw',withdraw_amount)
                if transaction_result['status'] == 0:
                    print('成功提现%s元，余额还有%s'%(withdraw_amount,account_data['data']['balance']))
                else:
                    print(transaction_result)
            else:
                print('余额不足，可提取%s元'%int(account_data['data']['balance']/2))
        if withdraw_amount == 'b'.lower():
            flag_exit = True
@auth
def pay_back(account_data,*args,**kwargs):
    '还款'
    trans_logger = kwargs.get('transaction_logger')
    print('账户余额'.center(50, '*'))
    print('credit:%s\n'
          'blance:%s' % (account_data['data']['credit'], account_data['data']['balance']))
    flag_exit = False
    while not flag_exit:
        payback_amount = input('请输入还款的金额按B返回：').strip()
        if len(payback_amount) > 0 and payback_amount.isdigit():
            payback_amount = int(payback_amount)
            transaction_result = make_transfer(trans_logger, account_data, 'repay', payback_amount)
            if transaction_result['status'] == 0:
                print('成功还款%s元，当前余额还有%s' % (payback_amount, account_data['data']['balance']))
            else:
                print(transaction_result)
        else:
            print('输入错误，请重新输入！')
        if payback_amount == 'b'.lower():
            flag_exit = True