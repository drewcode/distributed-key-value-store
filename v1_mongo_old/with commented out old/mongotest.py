from pymongo import MongoClient

client = MongoClient()
db = client.test

db.randomcoll.insert({'val' : '789','key' : 'zxc'})

query = raw_input('Enter key : ')

cursor = db.randomcoll.find({'key' : query})
for record in cursor:
	print record['val']