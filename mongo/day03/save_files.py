from  pymongo import MongoClient
import bson.binary

conn = MongoClient("localhost", 27017)

db = conn.grid

myset = db.image

f = open("10(1).jpg", "rb")

data = f.read()

#将文件往mongo中存储的时候， python　字节串转化为 bson binary
# data = bson.binary.Binary(data)
# myset.insert_one({"filename":"timg.jpg", "data":data})

#从mongo中读出二进制文件，并写到本地的时候，无需转化
img = myset.find_one({"filename":"timg.jpg"})
with open("timg.jpg", "wb") as f:
    f.write(img["data"])

conn.close()
