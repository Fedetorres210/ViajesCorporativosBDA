from config.connection import realizarConeccionViajes,realizarConeccionUsuarios

"""
Funcion que inserta un valor en la base de datos
@param un diccionario de valores
@return True si tiene exito o False

"""
def insertarViaje(datos):
    collection = realizarConeccionViajes()
    if  (collection==False):
        return False
    
   
    print(datos)
    resultados = collection.insert_one(datos)
    print(resultados)
    print(resultados,resultados.inserted_id)
    return True
    
    



"""
Verifica el inicio de sesion de un usuario
@param diccionario de valores para ser filtrado la query
@return Boolean


"""


def verificarInicioSesion(filtro):
    collection = realizarConeccionUsuarios()
    if (collection== False):
        return False
    try:
        usuario_encontrado = collection.find_one(filtro)
        if usuario_encontrado:  
            return True
        else:return False

    except Exception:
        return False





def verificarDato(filtro,collection):
    if (collection== False):
        return False
    try:
        usuario_encontrado = collection.find_one(filtro)
        
        if usuario_encontrado:
            print(usuario_encontrado)
            return usuario_encontrado
        else:return False

    except Exception:
        return False
    


def verificarDatos(filtro, collection):
    
    if (collection== False):
        return False
    try:
        
        usuario_encontrado = collection.find(filtro)
        if usuario_encontrado:
            return usuario_encontrado
        else:return False

    except Exception:
        
        return False




def encontrarColaborador(filtro):
    collection = realizarConeccionUsuarios()
    if (collection== False):
        return False
    try:
        usuario_encontrado = collection.find_one(filtro)
        if usuario_encontrado:  
            return True
        else:return False

    except Exception:
        return False



def generarColaborador(usuario,filtro):
    collection = realizarConeccionUsuarios()
    print(usuario,filtro)
    usuario_encontrado = collection.update_one(usuario,{"$set":filtro})
    print("Se realizo con exito")
    return usuario_encontrado

    
    


    
    
def insertarUsuario(datos):
    collection = realizarConeccionUsuarios()
    if  (collection==False):
        return False
    resultados = collection.insert_one(datos)
    return True



def encontrarViajesUsuario(filtro):
    collection = realizarConeccionViajes()
    usuario_encontrado = collection.find({"Colaborador.correo": filtro.getCorreo(), "Colaborador.password": filtro.getPassword()})
    print("Se realizo con exito")
    return usuario_encontrado

    
def eliminarViaje(filtro):
    collection = realizarConeccionViajes()
    collection.delete_one(filtro)


def modificarViaje(viaje,filtro):
    collection = realizarConeccionViajes()
    collection.update_one(viaje,{"$set":filtro})
    

    
