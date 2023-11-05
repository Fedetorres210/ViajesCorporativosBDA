from config.connection import realizarConeccionViajes, realizarConeccionUsuarios


def insertarViaje(datos):
    collection = realizarConeccionViajes()
    if  (collection == False):
        return False
    resultados = collection.insert_one(datos)
    print(resultados)
    print(resultados,resultados.inserted_id)
    return True
    

def verificarInicioSesion(filtro):
    collection = realizarConeccionUsuarios()
    if (collection == False):
        return False
    try:
        usuario_encontrado = collection.find_one(filtro)
        if usuario_encontrado:  
            return True
        else:return False

    except Exception:
        return False


def verificarDato(filtro,collection):
    if (collection == False):
        return False
    try:
        usuario_encontrado = collection.find_one(filtro)
        if usuario_encontrado:
            print(usuario_encontrado)
            return usuario_encontrado
        else: 
            return False

    except Exception:
        return False
    

def verificarDatos(filtro, collection):
    if (collection == False):
        return False
    try:
        usuario_encontrado = collection.find(filtro)
        if usuario_encontrado:
            return usuario_encontrado
        else:
            return False
    except Exception:
        return False


def encontrarColaborador(filtro):
    collection = realizarConeccionUsuarios()
    if (collection == False):
        return False
    try:
        usuario_encontrado = collection.find_one(filtro)
        if usuario_encontrado:  
            return True
        else:
            return False
    except Exception:
        return False


def generarColaborador(usuario,filtro):
    collection = realizarConeccionUsuarios()
    print(usuario,filtro)
    usuario_encontrado = collection.update_one(usuario,{"$set":filtro})
    print("Se realizó con exito")
    return usuario_encontrado


def insertarUsuario(datos):
    collection = realizarConeccionUsuarios()
    if  (collection == False):
        return False
    resultados = collection.insert_one(datos)
    return True


def encontrarViajesUsuario(filtro):
    collection = realizarConeccionViajes()
    usuario_encontrado = collection.find({"Colaborador.correo": filtro.getCorreo(), "Colaborador.password": filtro.getPassword()})
    print("Se realizó con exito")
    return usuario_encontrado


def encontrarViajesPendientes():
    collection = realizarConeccionViajes()
    viajes = collection.find({"estado": "pendiente"})
    print("Se realizó con éxito")
    print(viajes)
    return viajes


def eliminarViaje(filtro):
    collection = realizarConeccionViajes()
    collection.delete_one(filtro)


def modificarViaje(viaje, filtro):
    collection = realizarConeccionViajes()
    collection.update_one(viaje,{"$set":filtro})


def consultarViajesProgramados(mes, ano):
    collection = realizarConeccionViajes()

    
    # print(camposProyectados)
    viajesProgramados = collection.find()
    viajesProgramados = [elem for elem in viajesProgramados]
        
    viajesProgramados = verificarYearYMes(ano,mes,viajesProgramados)
    return viajesProgramados


def verificarYearYMes(anoEsperado, mesEsperado,datos):
    viajesEnFecha = []
    print("Entra a la funcion")
    
    if mesEsperado < 10:
        mesEsperado = "0" + str(mesEsperado)
    else:
        mesEsperado = str(mesEsperado)
    for elem in datos:
        
        if elem["fechaInicio"][0:4] == str(anoEsperado) and elem["fechaInicio"][5:7]== mesEsperado:
            viajesEnFecha.append(elem)
    return viajesEnFecha


def consultarViajesInternacional(trimestre,ano):
    collection = realizarConeccionViajes()
    viajesProgramados = collection.find({"esInternacional":"Si"})
    viajesProgramados = [elem for elem in viajesProgramados]
    
    viajesProgramados = verificarViajesTrimestreYAno(trimestre,ano,viajesProgramados)
    return viajesProgramados




def verificarViajesTrimestreYAno(trimestre,ano,datos):
    tr = { 
        "1er Trimestre":["01","02","03"],
        "2do Trimestre":["04","05","06"],
        "3er Trimestre":["07","08","09"],
        "4to Trimestre":["10","11","12"]
        }
    lista = []
    print(datos[-1])
    for elem in datos:
        print(elem["fechaInicio"][0:4]== str(ano))

        if elem["fechaInicio"][0:4] == str(ano) or elem["fechaFin"][0:4] == str(ano):  
               
            if elem["fechaInicio"][5:7] in tr[trimestre] or elem["fechaFin"][5:7] in tr[trimestre]:
                
                lista.append(elem)

    return lista    
        
        
        
    
        
def encontrarDestinos():
    colleccion = realizarConeccionViajes()  
    viajes = colleccion.distinct("destino")
    return viajes