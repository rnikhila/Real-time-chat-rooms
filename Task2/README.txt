README for Task 2  

Tested on Ubuntu 16.04, python 3.6
Please install the latest version Redis and Mongo DB

Check if Mongo is running on your localhost on port 27017
Check if Redis is running on your localhost on 6379
Install modules of both redis and mongodb :sudo pip install redis, python -m pip install pymongo
To run the code please type the following on command line when inside the Task2 folder :
python message_boards.py

Install Redis 

On Ubuntu Download, extract and compile Redis with:

$ wget http://download.redis.io/releases/redis-5.0.0.tar.gz
$ tar xzf redis-5.0.0.tar.gz
$ cd redis-5.0.0
$ make

The binaries that are now compiled are available in the src directory. Run Redis with:

$ src/redis-server

Install MongoDB

sudo apt-get install -y mongodb-org
To start MongoDB service
sudo service mongod start

Both Redis and MongoDB should be running on their default port

To simulate different user message boards execute:
python message_boards.py
select <board_name> [for selecting message board]
write <message> [write to the message board; after selecting the message board]
read [get history of the message board; after selecting the message board]
listen [listen to updates; after selecting the message board]
<Ctrl-C> [stop listening to updates]
stop [to exit]
