#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/26 21:06
File:admin
Author:liuyang97
'''
from config import setting
import os
import json
from .db_handler import save_db
from .loggers import logger_log

admin_logger = logger_log('admin')

def add_account(account):
    '增加账户'
    dic = {
        'id':None,
        'password':None,
        "credit":None,
        "balance": None,
        "enroll_date":None,
        "expire_date": None,
        "pay_day": None,
        "status": 0
    }
    account_file = os.path.join(setting.BASE_DB, '%s.json' %account)
    print(account_file)
    if os.path.isfile(account_file):
        print('账户已存在！')
    else:
        add_id = input('id:').strip()
        if add_id.isdigit():
            add_id = int(add_id)
        add_passwd = input('passwd:').strip()
        add_credit = input('credit:').strip()
        if add_credit.isdigit():
            add_credit = int(add_credit)
        balance = input('balance:').strip()
        if balance.isdigit():
            balance = int(balance)
        enroll_date = input('enroll_date:').strip()
        expire_date = input('expire_date:').strip()
        pay_day = input('pay_day:').strip()
        if pay_day.isdigit():
            pay_day = int(pay_day)
        dic['id'] = add_id
        dic['password'] = add_passwd
        dic['credit'] = add_credit
        dic['balance'] = balance
        dic['enroll_date'] = enroll_date
        dic['expire_date'] = expire_date
        dic['pay_day'] = pay_day
        f = open(os.path.join(setting.BASE_DB,'%s.json'%dic['id']),'w')
        json.dump(dic,f)
        f.close()
        print('账户已添加成功！')
        admin_logger.info('账户：%s已成功添加,信用额为%s元'%(dic['id'],dic['credit']))


def modify_line(account):
    '修改信用额度'
    account_file = os.listdir(setting.BASE_DB)
    modify_file = input('请输入要修改的账号：').strip()
    modify_file = '%s.json'%modify_file
    for i,v in enumerate(account_file):
        if modify_file == v:
            f = open(os.path.join(setting.BASE_DB,v),'r')
            data = json.load(f)
            f.close()
            print('当前额度%s元'%data['credit'])
            modifyline = input('请输入修改的额度：').strip()
            if modifyline.isdigit():
                modifyline = int(modifyline)
            data['credit'] = modifyline
            save_db(data)
            print('已成功修改%s额度,目前信用额度为%s元'%(modify_file,data['credit']))
            admin_logger.info('已成功修改账户:%s额度,目前信用额度为%s元'%(modify_file,data['credit']))

def unfreeze_account(account):
    '账户解锁'
    unfreeze_file = os.listdir(setting.BASE_DB)
    unfreeze = input('请输入要修改的账号：').strip()
    unfreeze = '%s.json'%unfreeze
    for i,v in enumerate(unfreeze_file):
        if unfreeze == v:
            f = open(os.path.join(setting.BASE_DB,v),'r')
            data = json.load(f)
            f.close()
            unfreeze_acc = input('是否解冻账号：').strip()
            if unfreeze_acc == 'y'.lower():
                data['status'] = 0
                print('账户:%s已解冻'%unfreeze)
            else:
                print('输入错误！')
            save_db(data)
            admin_logger.info('账户:%s已解冻'%unfreeze)
admin_msg = [
    ('账户添加',add_account),
    ('修改额度',modify_line),
    ('解冻账户',unfreeze_account)
]
def admin_load(account,*args,**kwargs):
    admin_id = account['data']['id']
    if admin_id == 8888:
        for i, v in enumerate(admin_msg):
            print(i, v[0])
        choice = input('请选择|q退出：').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(admin_msg) and choice >= 0:
                admin_msg[choice][1](account)
        elif choice == 'q'.lower():
              exit()
    else:
        print('不是管理员！')
        exit()