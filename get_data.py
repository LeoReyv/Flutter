from pymongo import MongoClient

from dateutil import parser
#expiry_date = '2021-07-13T00:00:00.000Z'
#expiry = parser.parse(expiry_date)


from datetime import datetime

def get_database():

   start_time = datetime.now()
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://leobardoreyv:Madseason_0610@cluster0.6e6sqec.mongodb.net/test"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   end_time = datetime.now()
   print('Duration: {}'.format(end_time - start_time))
   return client['pythonDB']

def get_collection():
   dbname= get_database()
   return(dbname["productos"] )




def get_cliente(cliente:str):
   dic_con =[]
        
   #collection_name=dbname["productos"]

   collection_name= get_collection()
   for n in collection_name.find({"cliente":str(cliente)}):
      dic_con=n['lista']

   

   return(dic_con)



  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   
   dbname = get_database()