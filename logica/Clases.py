

"""
Clase Usuario

"""
class Usuario:

    """
    Constructor de la clase Usuario
    @param self: self parametro propio de las clases en Python
    @param correo: correo correo electrnico del usuario este va servir para ingresar
    @param password: password clave del usuario
    
    """

    def __init__(self,correo,password,tipo):
        self.correo = correo
        self.password = password
        self.tipo = tipo


    """
    Metodo para generarDatos en un diccionario para se ingresados a mongo
    @param self: self parametro propio de las clases en Python
    @return devuele el diccionario con los atributos de la clase
    
    """
    def generarDatosjson(self):
        dic = { 
            "correo": self.correo,
            "password": self.password,
            "tipo": self.tipo
        }
        return dic
    
    def getCorreo(self):
        return self.correo
    
    def getPassword(self):
        return self.password
    
    def getTipo(self):
        return self.tipo


"""
Clase Colaborador que hereda de  Usuario


"""
class Colaborador(Usuario):

    """
    Constructor de la clase Colaborador que integra la superclase
    @param self: self parametro propio de las clases en Python
    @param correo: correo correo electrnico del usuario este va servir para ingresar
    @param password: password clave del usuario
    @param nombre: nombre nombre del colaborador
    @param puesto:puesto puesto del colaborador
    @param departamento departamento del colaborador
    @ viajes del colaborador
    
    """

    def __init__(self, correo, tipo, password,nombre, puesto,departamento):
        super().__init__(correo, password,tipo)
        self.nombre = nombre
        self.puesto = puesto
        self.departamento = departamento

    """
    Metodo para generarDatos en un diccionario para se ingresados a mongo
    @param self: self parametro propio de las clases en Python
    @return devuele el diccionario con los atributos de la clase
    """
    

    def generarDatosjson(self):
        dic = super().generarDatosjson()
        dic["informacion"] =  {
            "nombre": self.nombre,
            "puesto": self.puesto,
            "departamento": self.departamento,
            

        }

        return dic
    

    """
    Metodo para asignar un viaje a la lista total de viajes del colaborador
    """
    

    def asignarViaje(self,viaje):
        self.viajes = self.viajes.append(viaje)

    def getNombre(self):
        return self.nombre
    

    def getPuesto(self):
        return self.puesto
    

    def getDepartamento(self):
        return self.departamento
    
    def getViajes(self):
        return self.viajes





"""

Clase Funcionario que hereda de Usuario

"""
class Funcionario(Usuario):
    def __init__(self, correo, password,nombre):
        super().__init__(correo, password)




"""
Clase Viaje 


"""

class Viaje:

    """
    Constructor de la clase Viaje
    @param self: self parametro propio de las clases en Python
    @param colaborador:colaborador colaborador de tipo Colaborador que tiene la informacion del colaborador
    @param internacional: internacional si el tiquete del viaje es internacional o no
    @param destino: destino del viaje
    @param fechaInicio: fecha de inicio del viaje
    @param fechaFin : fecha de terminacion del viaje
    @param detalles: detalles del viaje
    @param: aerolinea: aerolinea del viaje
    @param precio: precio del viaje
    
    
    """
    def __init__(self,colaborador,internacional,destino,motivo,fechaInicio,fechaFin,aerolinea,precio,alojamiento,transporte):
        self.colaborador = colaborador
        self.internacional = internacional
        self.destino = destino
        self.motivo =motivo
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        
        self.aerolinea = aerolinea
        self.precio = precio
        self.alojamiento =alojamiento
        self.transporte = transporte

    def generarDatosJSON(self):
        dic = {
            "Colaborador":self.colaborador.generarDatosjson(),
            "esInternacional": self.internacional,
            "destino": self.destino,
            "motivo":self.motivo,
            "fechaInicio":f"{self.fechaInicio}",
            "fechaFin":f"{self.fechaFin}",
            "aerolinea":self.aerolinea,
            "precio":self.precio

        }

        return dic
    


    
    

        

    


    