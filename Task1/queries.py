from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint


collection = connectMongo()

##### FIND ALL ENTRIES IN THE DATABASE #####
# Assuming RQ0 is the query to find all entries in the database
RQ0 = collection.find()
for data in RQ0:
	pprint.pprint(data)
########
###WQ1 adding dummy_fitness.json to mongodb####

with open("dummy-fitness.json") as json_data:
	data = json.load(json_data)
for item in data:
	collection.insert(item)
print("done with WQ1")
###########
###WQ2 updating db for user 1001 
collection.update(
   { "uid": 1001 },
   {
	 '$set': 
	 {
	   "height": "5ft10in",
	   "weight": "190lbs",
	   "tags": [ "ambitious" ]
	 }
   }
)
print("done with WQ2")

#####RQ1 - Number of employees #####
print("number of employees in AggiefitDB",len(collection.distinct("uid"))) 
print("done with RQ1")
##### RQ2 - printing employees with irregular tags 
RQ2=collection.find({"tags":"irregular"},{"uid":1})
for col in RQ2:
	pprint.pprint(col)
print("done with RQ2")
##### RQ3 - employees with goal steps less than or equal to 1500
RQ3 = collection.find({"goal.stepGoal": {'$lte':1500}},{"uid": 1})
for col in RQ3:
	pprint.pprint(col)
print("done with RQ3")	
##### RQ4 - reporting activity duration of employees
RQ4 = collection.aggregate([
	{
	'$project':{
		"totalActivityDuration":{"$sum":"$activityDuration"}
	}
	}
	])
for col in RQ4:
	pprint.pprint(col)
print("done with RQ4")
