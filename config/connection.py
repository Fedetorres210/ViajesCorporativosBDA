import pymongo


"""
Funcion que realiza la conexion con la base de datos
@param URL de la base de datos
@param autenticacion de la base de datos
@param usuario de la base de datos
@password de la base de datos
return una coneccion con una coleccion dee mongoDB o un False en caso de error

"""
def realizarConeccion(URL= "localhost:27017", AUTH = None, username = None, password = None):
    try:   
        client = pymongo.MongoClient(URL)
        db = client.viajes
        collection = db.viajesCorporativos

    except Exception:
        return False
    
    
    return collection



    

