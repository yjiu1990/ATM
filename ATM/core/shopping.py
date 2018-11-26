#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/24 19:10
File:shopping
Author:liuyang97
'''
from  .make import make_transfer
from .db_handler import save_db
from .loggers import logger_log
from.auth import auth


shopping_logger = logger_log('shopping')
def shoppings(account_data,*args,**kwargs):
    trans_logger = kwargs.get('transaction_logger')
    exit_flag = False
    goods = [
        ["电脑", 1999],
        ["鼠标", 10],
        ["游艇", 20],
        ["美女", 998],
    ]

    shopping_list = {}
    while not exit_flag:
        print('-----------商品列表-------')
        for i, v in enumerate(goods):
            print(i, v)

        choice = input('请输入商品的编号|q退出|y结账：').strip()

        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(goods):
                product = goods[choice]

                if product[0] in shopping_list:
                    shopping_list[product[0]][1] += 1
                else:
                    shopping_list[ product[0] ] =[ product[1],1]
                    print('%s已成功加入购物车'%product[0])

        elif choice == 'y'.lower():
                buckles_money(account_data,shopping_list)
        elif choice == 'q'.lower():
            break
@auth
def buckles_money(account_data,shopping_list,*args,**kwargs):
    print('购物车清单'.center(50, '*'))
    id_cat = 1
    total = 0
    print('id\t商品\t数量\t单价\t总价')
    for key in shopping_list:
        print('%s\t%s\t%s\t%s\t%s' % (id_cat,
                                      key,
                                      shopping_list[key][1],
                                      shopping_list[key][0],
                                      shopping_list[key][1] * shopping_list[key][0]))
        id_cat += 1
        total += shopping_list[key][1] * shopping_list[key][0]
    print('END'.center(50,'*'))
    flag_exit = False
    while not flag_exit:
        settle_acount = input('是否买单|y是|q退出：').strip()
        if settle_acount == 'y':
            print('账户余额'.center(50, '*'))
            print('credit:%s\n'
                  'blance:%s' % (account_data['data']['credit'], account_data['data']['balance']))
            old_balance = account_data['data']['balance']
            if total <= old_balance:
                new_balance = old_balance - total
                print('已购买成功,您总共花了%s元,现在余额是%s元'%(total,new_balance))
                account_data['data']['balance'] = round(new_balance,2)
                save_db(account_data['data'])
                shopping_logger.info('account:%s consume:%s  balance:%s' %
                                     (account_data['data']['id'], total, new_balance))
                exit()

            else:
                print('余额不足,您现在的余额是%s元'% round(account_data['data']['balance'],2))

        elif settle_acount == 'q':
                exit()
