from config.connection import realizarConeccion

"""
Funcion que inserta un valor en la base de datos
@param un diccionario de valores
@return True si tiene exito o False

"""
def insertarValor(datos):
    collection = realizarConeccion()
    if  (collection==False):
        return False
    
    try:
        resultados = collection.insert_one(datos)
        print(resultados)
        print(resultados,resultados.inserted_id)
        return True
    except Exception:
        return False
    



"""
Verifica el inicio de sesion de un usuario
@param diccionario de valores para ser filtrado la query
@return Boolean


"""


def verificarInicioSesion(filtro):
    collection = realizarConeccion()
    if (collection== False):
        return False
    try:
        usuario_encontrado = collection.find_one(filtro)
        if usuario_encontrado:  
            return True
        else:return False

    except Exception:
        return False





def verificarDato(filtro):
    collection = realizarConeccion()
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
    


def verificarDatos(filtro):
    collection = realizarConeccion()
    if (collection== False):
        return False
    try:
        usuario_encontrado = collection.find(filtro)
        if usuario_encontrado:
            return usuario_encontrado
        else:return False

    except Exception:
        return False





    


    
    






    

    
