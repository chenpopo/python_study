import pymongo

#建立数据库连接
conn = pymongo.MongoClient("localhost", 27017)

#创建数据库对象
db = conn.db

#创建数据集合对象
myset = db.class0

#数据操作：增删改查索引聚合
# print(dir(myset))


#myset.insert_one({"name":"张铁林", "King":"乾隆"})
# myset.insert_many([
#                         {"name":"张国立", "King":"康熙"},
#                         {"name":"陈道明", "King":"康熙"}
#                     ])
# myset.save({"_id":1, "name":"聂远","King":"乾隆"}) #save方法如果_id重复，会覆盖数据库对应文档

#遍历游标查询数据,
# concur = myset.find({"King":"康熙"},{"_id":0})
# for i in concur:
#     print(i["name"])

# data = myset.find_one({"name":{"$gt":"张国立"}}, {"_id":0})
# print(data)

# concur = myset.find({},{"_id":0})
# for i in concur.skip(9).limit(3):
#     print(i)

# concur = myset.find({},{"_id":0})
# for i in concur.sort([("name",1)]):
#     print(i)

#更新操作
#myset.update_one({"name":"郑少秋"}, {"$set":{"King":"乾隆"}}, upsert=True)
#myset.update_many({"King":"康熙"}, {"$set":{"KingName":"玄烨"}})
#myset.update({"King":"乾隆"}, {"$set":{"KingName":"弘历"}}, multi=True)

#删除操作
# myset.delete_one({"gender":None})
# myset.delete_many({"age":{"$gt":24}})
# myset.remove({"age":20}, multi=False)

#创建索引
# myset.create_index("name")
# indexes = myset.list_indexes()
# for i in indexes:
#     print(i)

#聚合操作
l = [
    {"$group":{"_id":"$King", "num":{"$sum":1}}}, #跟King域进行分组，统计每组数量为num
    {"$sort":{"num":-1}}    #根据每组数量进行排序
]

#关闭数据库连接
conn.close()