from pymongo import MongoClient

from dateutil import parser

import datetime
from dateutil import parser

fecha_registro = datetime.datetime.now()


from datetime import datetime


# def main():
   
   
#    # dbname=dbase
#    dic =[]
#    m=[]
      

#    test=get_precios()
#    #test= get_database()
#    if test is None:
#       print("base de datos vacia")

#    dic=test.find({"nombre":"atun"})
#    for b in dic:
#       if b["nombre"]== "atun":
#          print("encontrado")
#          print(b["precio"])
         
   
   

  # test.find({"lista.producto.nombre":"coca"})
   #data= test["registros"].find({"cliente":"luis","lista.producto.nombre":"coca"})
   # if test3.collection.count_documents is None:
   #    print("con coleccion")
   # for n in test3:
   #    dic=n['lista']
   # for f in dic:
   #    m=f["producto"]
   # print(m)
   # for b in data:
   #    dic.append(b)
   # for x in dic:
   #    m.append(x)
   # print(m)
   
   
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
      dbname=dbase
      # if dbname is None:
      #dbname = get_database() 
      
      
      return(dbname["productos"] )
   except Exception as e:
      return(False)

def get_precios(producto):
   try:
      dbname=dbase
      test=dbname["registros"]
      dic=test.find({"nombre":producto})
      for b in dic:
         if b["nombre"]== producto:
            print("encontrado")
            prec=b["precio"]
         
      return(prec)
      #precio=db
      
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
      if dbname is None:
         dbase = get_database() 
         dbname = dbase
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
      dbname = get_database()
      return True
   except Exception as e:
      print("Ocurrio una Problema::",e)
      return False
   finally:
      dbname = get_database()



    
def lista_compras(nombre, precio):
    
    try:
        dbname = get_database()
        collection_name = dbname["registros"]

        print(fecha_registro)
        print("Conexion")
        registro = {
            
            "fecha":fecha_registro,
            
            "cliente": nombre,


            "total": precio,
                
                    
                }
   

        collection_name.insert_one(registro)
        return True
    except Exception as e:
        print("Ocurrio una excepcion::",e)
        return False
  
# This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":   
  
#    # Get the database
   
#    dbase = get_database()
#    # dbname=dbase
   
#    main()
   
   