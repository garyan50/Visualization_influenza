import pymongo
import os
import json

path = 'e:\\mongodata\\JSON\\tweet-2019JulToSep\\tweet'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["FluRelatedTweets2019JulToSep"]
mycol = mydb["tweet"]

json_list = []
print('Loading json files...\n')
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        file_path = os.path.join(r, file)
        with open(file_path, 'rb') as data_file:
            data_json = json.load(data_file)
            json_list.append(data_json)

print('Finished loading. Start bulk writing...')
mycol.insert_many(json_list)
