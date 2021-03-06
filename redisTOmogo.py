# Import the needed packages
import pymongo as mongo
import redis
from bs4 import BeautifulSoup
from time import sleep
import multiprocessing

# Make a connection with redis
connect = redis.Redis()

# Make connection to your database without security
client = mongo.MongoClient("mongodb://127.0.0.1:27017")

# Connect to the existing names
database = client["Blockchain"]
collection = database["BlockchainedV2"]

# Make new list or arrays
hashes = []
times = []
btcs = []
usds = []

# Make a function
def calculatrix(connect, DataInBase):

    #Fill in your lists or arrays
    hashes = list(map(str, connect.lrange("Hash", 0, -1)))
    times = list(map(str, connect.lrange("Time", 0, -1)))
    btcs = list(map(float, connect.lrange("Amount(BTC)", 0, -1)))
    usds = list(map(float, connect.lrange("Amount(USD)", 0, -1)))

    #Pass on the values
    USD = max(usds)
    index = usds.index(USD)
    hash = hashes[index]
    timed = times[index]
    btc = btcs[index]

    #all values in dictionary to make it easier for outputting
    dict = {"Hash": hash, "Time": timed, "Amount(BTC)": btc, "Amount(USD)": USD }
    
    #Store output in DB
    DataInBase.insert_one(dict)
    
# Call youre function and overwrite every 60 seconds
while True:
    calculatrix(connect, collection)
    sleep(60)
