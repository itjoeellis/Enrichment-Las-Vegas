from pymongo import MongoClient
import configuration
connection_params = configuration.connection_params

#connect to mongodb
mongoconnection = MongoClient(
    'mongodb://127.0.0.1:27017/'
)
print("Connection Successful")



db = mongoconnection.databasename
