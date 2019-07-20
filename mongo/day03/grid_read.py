import pymongo
import gridfs

#连接数据库
conn = pymongo.MongoClient("localhost", 27017)

#生产数据库对象
db = conn.grid

#生产集合对象
myset = gridfs.GridFS(db)

#从数据库中读取文件
files = myset.find({"filename":"view.jpg"})
for file in files:
    print(file)
    with open(file.filename,"wb") as f:
        f.write(file.read())
