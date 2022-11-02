# -*- coding: utf-8-*-
# @time     : 2022/10/24  17:50
# @Author   : liz

# logging是什么?作用是什么?
# logging--是Python自带的一个日志模块。
# 1它的作用主要是有两个:
# 1)代替print,可以把大部分你想要进行调试的信息打印出来或者是输出到指定文件.
# 2)可以对一些输出的调试信息分类做输出,比如说:
# DEBUG, INFO, WARNING, ERROR, CRITICAL
#级别从左到右，由低到高

# 关于日志的这个级别的定义,大家之后还是需要自己去自行进行拓展!!!
# 一般都是看你对日志的级别定义是怎样就设置为哪个级别的。

import logging
# from tools.project_path import *

#Logger日 debug info error
# #handdler 输出日志的渠道 指定的文件 还是控制台

# logging.debug("这是debug")
# logging.info("这是info")
# logging.warning("警告")
# logging.error("错误")
# logging.critical("这是critical")

#定义一个日志收集器my_logger
my_logger=logging.getLogger("my")

#设置级别
my_logger.setLevel("DEBUG")

#设置日志输出格式
formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")


#创建一个自己的输出渠道
ch=logging.StreamHandler()# 输出到控制台
ch.setLevel("DEBUG")# 设置级别
ch.setFormatter(formatter)# 设置输出格式
   
#指定输出到文本文件 渠道
# fh=logging.FileHandler(log_record, encoding="UTF-8")
# fh.setLevel("ERROR")
# fh.setFormatter(formatter)

#两者对接
my_logger.addHandler(ch)
# my_logger.addHandler(fh)

#收集日志
my_logger.debug("这是debug")
my_logger.info("这是info")
my_logger.error("错误！错误！")
my_logger.critical("这是critical")


#Formatter 常用信息
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别 类似 DEBUG INFO ERROR
# %(pathname)s 调用日志输出函数的模块的完整路径名,可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间,用UNIX标准的表示时间的浮点数表示
#%(relativeCreated)d|输出日志信息时的,自Logger创建以 来的毫秒数
# %(asctime)s字符串形式的当前时间。默认格式是"2003-07-08 16:49:45,896",逗号后面的是毫秒
# %(thread)d线程ID。可能没有
# %(threadName)s1线程名。可能没有
# %(process)d进程ID,可能没有
# %(message)s用户输出的消息