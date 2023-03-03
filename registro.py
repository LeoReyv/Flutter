from get_data import get_database

from pymongo  import errors
from pymongo import MongoClient
import datetime
from dateutil import parser

fecha_registro = datetime.datetime.now()

def main():
    print(registro_producto("azucar",30))
    
def registro_producto(nombre, precio):
    
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
    
if __name__ == "__main__":   
  
   # Get the database
   
    shRet = 0
    shRet = main()