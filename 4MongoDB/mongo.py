from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient('localhost',27017)

# 创建数据库对象
db = conn.stu 

# 创建集合对象
myset = db.class4

# 数据操作

# *****************insert*********************
# myset.insert_one({'name':'张铁林','King':'乾隆'})
# myset.insert_many([{'name':'张国立','King':'康熙'},\
#     {'name':'陈道明','King':'康熙'}])
# myset.insert({'name':'唐国强','King':'雍正'})
# myset.insert([{'name':'陈建斌','King':'雍正'},\
#     {'_id':1,'name':'吴奇隆','King':'四爷'}])
# myset.save({'_id':1,'name':'聂远','King':'乾隆'})

# ****************find********************
# cursor=myset.find({'name':{'$exists':True}},{'_id':0})
# for i in cursor:
#     print(i['name'],'--',i['King'])

# print(cursor.next()) #打印下一条文档

#取前三条
# for i in cursor.limit(3).sort([('name',1)]):
#     print(i)

# dic = {'$or':[{'King':'乾隆'},{'name':'陈道明'}]}
# d = myset.find_one(dic)
# print(d)

# ******************update****************
# myset.update_many({'King':'康熙'},\
#     {'$set':{'king_name':'玄烨'}})
# myset.update_one({'King':'雍正'},\
#     {'$set':{'king_name':'胤禛'}})
# myset.update_one({'name':'郑少秋'},\
#     {'$set':{'King':'乾隆'}},upsert=True)

# myset.update({'King':'乾隆'},\
#     {'$set':{'king_name':'弘历'}})

# ******************* delete *************
# myset.delete_one({'King':'康熙'})
# myset.delete_many({'King':'雍正'})
# myset.remove({'king_name':None})

# *************复合操作*******************
data = myset.find_one_and_delete({'name':'张铁林'})
print(data)

# 关闭连接
conn.close()