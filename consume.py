# -*- coding: utf-8 -*-
'''
Created on 2018年1月26日

@author: imac
'''
from db_utile import *


def get_queue(rc):
    data_source = rpop_data(rc, 'data');  #获取任务队列 
    push_data(rc, data_source[1].split('_')[1], '%s__%d' % (data_source,1))  # 假装修改一下，存储到另外一个 队列中表示已经完成
    print data_source
    
    

# 假装在这里源源不断取出任务
if __name__ == '__main__':
    rc =redis_client()
    while True:
        get_queue(rc)
        
    

