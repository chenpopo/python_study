import pymongo
import gridfs

#连接数据库
conn = pymongo.MongoClient("localhost", 27017)

#生产数据库对象
db = conn.grid

#生产集合对象
myset = gridfs.GridFS(db)

#将文件写入到数据库中
with open("10.jpg","rb") as f:
    myset.put(f.read(), filename="view10.jpg")
