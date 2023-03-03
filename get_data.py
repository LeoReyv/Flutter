from pymongo import MongoClient

from dateutil import parser

import datetime
from dateutil import parser

fecha_registro = datetime.datetime.now()


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
   try:
      dbname = get_database()
      return(dbname["productos"] )
   except Exception as e:
      return(False)

def get_precios():
   try:
      dbname = get_database()
      return(dbname["registros"])
   except Exception as es:
      return(False)
def get_cliente(cliente:str):
   dic_con =[]
        
   #

   collection_name= get_collection()
   for n in collection_name.find({"cliente":str(cliente)}):
      dic_con=n['lista']

   

   return(dic_con)

def registro_producto(nombre:str, precio:int|float):
    
    try:
        dbname = get_database()
        collection_name = dbname["registros"]

        print(fecha_registro)
        print("Conexion")
        registro = {
            "registro":{
            "fecha":fecha_registro,
            "producto" : {
            "nombre": nombre,
            "precio": precio,
                
                    }
                }
            }   

        collection_name.insert_one(registro)
        return True
    except Exception as e:
        print("Ocurrio una excepcion::",e)
        return False
    

  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   
   dbname = get_database()