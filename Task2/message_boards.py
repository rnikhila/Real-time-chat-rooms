import redis
import pymongo
import json
import pprint
import constants

from mongo_connect import connectMongo

r = redis.Redis()
collection = connectMongo()
subscribing = False;
mes_board = "";

while True:

	try:

		if subscribing:
			#true when listening


			for item in p.listen():	
				
				if item['type'] == 'subscribe':
					print(f"Subscribed to {str(item['channel'],'utf-8')} message board")
				if item['type'] == 'message':
					print(f"message received: {str(item['data'],'utf-8')}")



		cmd = input('please input a command (select/write/listen/read/stop)')
		cmd_parts = cmd.split(" ")
		cmd_parts[0] = cmd_parts[0].lower()


		if cmd_parts[0] == "select" and len(cmd_parts) > 1:
			mes_board = cmd_parts[1]
			print(f"Selecting message board {mes_board}")


		elif cmd_parts[0] == "read" and mes_board != "":

			MO = collection.find({ "message_board": mes_board })
			print(f"message board conversation history of {mes_board}:")
			for data in MO:
				for words in data['history']:
					print (words)


		elif cmd_parts[0] == "write" and mes_board != "":

			to_set = ' '.join(cmd_parts[1:])
			#storing every message to mongoDB
			collection.update(
					{'message_board': mes_board}, 
					{'$push': 
						{'history': to_set}
					}, True)

			#sending out messages to subscribers
			res = r.publish(mes_board, to_set) 
			print (f"message:{to_set} [sent to {res} user/s who is/are subscribed]") 

		elif cmd_parts[0] == "listen" and mes_board != "":

			subscribing = True;
			p = r.pubsub()
			res = p.subscribe([mes_board]) 
			if res and res['type'] == 'message':
				print (f"message board {res['channel']}: \n message:{res['data']}")

		elif cmd_parts[0] == "write" and mes_board == "":

			print("Please select a message board first!")

		elif cmd_parts[0] == "read" and mes_board == "":

			print("Please select a message board first!")

		
		elif cmd_parts[0] == "listen" and mes_board == "":

			print("Please select a message board first!")

		elif cmd_parts[0] == "stop":
			#exit
			break

		else:
			print("***********************************************")
			print("wrong input format, please try:")
			print("***********************************************")
			print("* select <board_name> [for selecting message board]")
			print("* write <message> [write to the message board; after selecting the message board]")
			print("* read [get history of the message board; after selecting the message board]")
			print("* listen [listen to updates; after selecting the message board]")
			print("* <Ctrl-C> [stop listening to updates] ")
			print("* stop [to exit]")




	except (KeyboardInterrupt) as e:

		subscribing = False
		