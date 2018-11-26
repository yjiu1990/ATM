#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/25 10:49
File:db_handler
Author:liuyang97
'''
import json,os
from config import setting

def load_account(account):
    '读取文件'
    account_file = os.path.join(setting.BASE_DB,'%s.json'%account)
    # print(account_file)
    if os.path.isfile(account_file):
        f = open(account_file)
        data = json.load(f)
        f.close()
        return {'status':0,'data':data}
    else:
        return {'status':-1,'error':'文件不存在'}

def save_db(account_data):
    '保存文件'
    account_file = os.path.join(setting.BASE_DB,'%s.json'%account_data['id'])
    # print(account_file)
    if os.path.isfile(account_file):
        f = open('%s.new'%account_file,'w')
        data = json.dump(account_data,f)
        f.close()
        os.remove(account_file)
        os.rename('%s.new'%account_file,account_file)
        return {'status':0,'data':data}
    else:
        return {'status':-1,'error':'文件不存在'}

