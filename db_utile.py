# -*- coding: utf-8 -*-
'''
Created on 2018年1月26日

@author: liqingju
'''
import redis

def redis_client():
    pool = redis.ConnectionPool(host='127.0.0.1', port='6379')
    return redis.Redis(connection_pool=pool) # host_redis.rpush('listone', '2')


# 把 需要处理的任务加入到任务队列 左进 进入 进入不在一个锁
def push_data(redis_client,queue_name,queue_data):
    redis_client.lpush(queue_name,queue_data) 
    
# 把 需要处理的任务加入到任务队列   右出 进入 进入不在一个锁
def rpop_data(redis_client,queue_name):
    return redis_client.brpop(queue_name,timeout=0)

# 每个任务生成唯一编号   
def get_id(redis_client,queue_id):
    return redis_client.incr(queue_id)
    
    
