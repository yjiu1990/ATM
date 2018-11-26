#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Time:2018/5/24 19:20
File:main
Author:liuyang97
'''
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    from core import main
    main.entrance()
