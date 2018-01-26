# -*- coding: utf-8 -*-
from db_utile import *
from time import sleep






# 把任务加到 待执行队列中
def add_queue(rc,data):
    id_queue =get_id(rc,'id_add')
    push_data(rc,"data",'%d_%s' % (id_queue,data));
    return  id



# 假装在这里填充任务
if __name__ == '__main__':
    data_int =0;
    rc = redis_client();
    while True:
        add_queue(rc,str(data_int))
        data_int =data_int+1;
        print data_int
        sleep(10)
    
    







