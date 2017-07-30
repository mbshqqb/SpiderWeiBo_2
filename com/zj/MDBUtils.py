#coding=utf-8
#
import json
import pymysql
import sys

import pymongo


#创建连接
def getDB():
    client = pymongo.MongoClient('172.17.11.169', 27017)
    db = client.admin
    db.authenticate("root", "root")
    db =client['zj']
    return db,client


def get(tablename, col, value):
    list = []
    dist = {}
    cursor = db.get_collection(tablename).find({col: {"$eq": value}}, {"_id": 0})
    for item in cursor:
        for key, value in item.items():
            dist[key] = value
        list.append(dist)
        dist = {}
    return list
def get_all(tablename, *cols):
    projection={"_id": 0}
    for col in cols:
        projection[col]=1
    cursor = db.get_collection(tablename).find({},projection)
    list = []
    dist = {}
    for item in cursor:
        for key, value in item.items():
            dist[key] = value
        list.append(dist)
        dist = {}
    return list

def insert(collist: object, data: object, table: object) -> object:
    # 设置唯一索引，去重操作
    collection = db.get_collection(table)
    counter=db.get_collection("counters")
    has_counter=False
    seq_name = None
    item = {}
    doc=counter.find_one({"name": table})
    if doc is not None:
        has_counter=True
        seq_name=str([key for key in doc.keys()][2])
        doc=counter.find_and_modify(query={"name": table}, update={"$inc": {seq_name: 1}},new=True)
        item[seq_name] = doc[seq_name]

    length=len(collist)
    for i in range(0,length):
        item[collist[i]]=data[i]
    try:
        collection.insert_one(item)
    except pymongo.errors.DuplicateKeyError:
        print('忽略插入重复数据')
        if has_counter:
            counter.find_and_modify(query={"name": table}, update={"$inc": {seq_name: -1}},new=True)
        return False
    return True

def end(client):
    client.close()

db,client=getDB()
db.get_collection("user_info").ensure_index("user_id", unique=True, dropDups=True)
db.get_collection("weibo_info").ensure_index("weibo_id", unique=True, dropDups=True)
db.get_collection("weibo_info_2").ensure_index("weibo_id", unique=True, dropDups=True)



