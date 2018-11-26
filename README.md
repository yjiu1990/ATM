# ATM
ATM作业
主程序---》main_server.py
目前已实现了查询账户信息、转账、还款、提款、购物商城和后台管理等功能，在后台管理因时间关系，只完成了账户添加
账户解锁与修改信用卡额度。
未完成的功能账户输入多次密码错误账户被锁定，还有新增个人密码修改功能等功能，以后有时间再进行完善
目录结构图
atm
│  ATM.pdf
│  main_server.py
│  README
│  tree.txt
│  __init__.py
│  
├─config 
│  │  setting.py  ---- 配置文件
│  │  __init__.py
│  │  
│  └─__pycache__
│          setting.cpython-36.pyc
│          __init__.cpython-36.pyc
│          
├─core
│  │  admin.py -- 后台管理
│  │  ATM_operation.py --- 交易中心
│  │  auth.py  --- 账户验证
│  │  db_handler.py --- 文件操作
│  │  loggers.py  --- 日志
│  │  main.py ---主程序入口
│  │  make.py  --- ATM操作
│  │  shopping.py --- 购物商城
│  │  __init__.py
│  │  
│  └─__pycache__
│          admin.cpython-36.pyc
│          ATM_operation.cpython-36.pyc
│          auth.cpython-36.pyc
│          db_handler.cpython-36.pyc
│          loggers.cpython-36.pyc
│          main.cpython-36.pyc
│          make.cpython-36.pyc
│          shopping.cpython-36.pyc
│          __init__.cpython-36.pyc
│  
│        
│          
├─db
│  │  __init__.py
│  │  
│  └─accounts --- 账户文件
│          12.json
│          123.json
│          1234.json
│          14.json
│          admin.json
│          __init__.py
│          
├─log
│  │  access.log --- 普通用户操作日志
│  │  admin.log --- 管理员操作日志
│  │  shopping.log ---- 消费日志
│  │  transaction.log ---- 交易日志
│  │  __init__.py
│  │  
│  └─__pycache__
│          __init__.cpython-36.pyc
│          
└─shopp
    │  __init__.py
    │  
    └─__pycache__
            __init__.cpython-36.pyc
