import pymongo
from random import randint

conn = pymongo.MongoClient("localhost", 27017)
db = conn.stu
myset = db.class_4

cursor = myset.find()
for i in cursor:
    print(i)
    # myset.update_one({"_id":i["_id"],},
    #                  {"$set":{"score":{"chinese":randint(66, 100),
    #                                    "math":randint(66, 100),
    #                                    "english":randint(66, 100)}
    #                           }
    #                   })

# myset.find({}, {"name":1, "score":1}).sort([{"score."}]{"score":1})

conn.close()