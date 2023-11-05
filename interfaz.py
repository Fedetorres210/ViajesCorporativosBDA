import streamlit as st
from  logica.Clases import Usuario, Viaje, Colaborador
from config.config import encontrarDestinos, encontrarViajesPendientes, insertarViaje, consultarViajesProgramados, verificarInicioSesion, verificarDato, encontrarColaborador, generarColaborador, insertarUsuario, verificarDatos, encontrarViajesUsuario, eliminarViaje, modificarViaje,consultarViajesInternacional 
from config.connection import realizarConeccionUsuarios, realizarConeccionViajes
import pandas as pd


if 'user' not in st.session_state:
    st.session_state.user = None

if 'colaborador' not in st.session_state:
    st.session_state.colaborador = None

pantallaInicio1 = st.container()
with pantallaInicio1:
    st.title("Sistema de Viajes")
    accion = st.selectbox("Seleccione su opción: ", ["...", "Crear Cuenta", "Iniciar Sesion"])
    if accion == "Iniciar Sesion":
        iniciarSesionC = st.container()
        with iniciarSesionC:
            correo = st.text_input('Ingrese su usuario o cedula:', key="input_cedula")
            clave = st.text_input("Ingrese su contraseña: ", key="inputClave")
            btnIniciarSesion = st.button("Iniciar sesión")

            if btnIniciarSesion:
                filtro = {"correo": correo, "password": clave}
                usuarioActual = verificarDato(filtro,realizarConeccionUsuarios()) 

                if usuarioActual:
                    usuarioActual = Usuario(usuarioActual['correo'], usuarioActual['password'], usuarioActual['tipo'])
                    st.success(f"Bienvenido de regreso {usuarioActual.getTipo()}")
                    st.session_state.user = usuarioActual

    if accion  == "Crear Cuenta":
        crearCuenta=st.container()
        with crearCuenta:
            st.text('Por favor, agregue la informacion solicitada:')
            correo = st.text_input("Correo:",key="input_correo")
            contrasena = st.text_input("Contraseña:",key="input_contraseña")
            tipo = st.selectbox("Selecciona el tipo de usuario",["Colaborador","Empleado"])
            btnCrearCliente=st.button("Crear Cliente")
            btnContinuar= st.button("Continuar")
            
            if btnCrearCliente:
                try: 
                    miUsuario = Usuario(correo,contrasena,tipo)
                    res = insertarUsuario(miUsuario.generarDatosjson())
                    if(res):
                        st.success("Se registro con exito la conexion")
                    else:
                        raise (Exception("Fallo en la conexion con la base de datos "))
                except:
                    st.warning("No se registro la informacion")


if st.session_state.user and st.session_state.user.getTipo() == "Colaborador":
    pantallaSolicitud = st.container()
    with pantallaSolicitud:
        st.title("Solicitudes")
        accion = st.selectbox("Seleccione su opcion: ",["...","Registro de una solicitud de viaje","Modificar/Eliminar una solicitud","Ver solicitud de solicitudes"])
        if accion == "Registro de una solicitud de viaje":
            registro = st.container()
            with registro:
                    columna1, columna2,columna3= st.columns(3)
                    with columna1:   
                        if st.session_state.colaborador:
                            nombreCompleto = st.text_input('Ingrese su nombre completo:',key="input_nombreCompleto",value = st.session_state.colaborador.getNombre())
                            puesto = st.text_input("Ingrese su puesto: ",key="inputPuesto",value = st.session_state.colaborador.getPuesto())
                            departamento = st.text_input("Ingrese el departamento en que trabaja: ",key="inputDepartamento",value = st.session_state.colaborador.getDepartamento())
                        else:
                            nombreCompleto = st.text_input('Ingrese su nombre completo:',key="input_nombreCompleto")
                            puesto = st.text_input("Ingrese su puesto: ",key="inputPuesto")
                            departamento = st.text_input("Ingrese el departamento en que trabaja: ",key="inputDepartamento")
                        
                        viajeInternacional= st.selectbox("Su viaje es internacional: ", ["...","Si", "No"])
                        pais = st.text_input("Ingrese pais destino: ",key="inputpais")
                        viaje = st.selectbox("Motivo de viaje: ",["...","Seguimiento","Cierre venta", "Capacitacion"])

                    with columna3:
                        fechaInicio = st.date_input("Ingrese la fecha de inicio: ")
                        fechaFin = st.date_input("Ingrese la fecha de finalizacion: ")
                        detalles = st.text("Detalles del vuelo")
                        aereolina = st.text_input("Ingrese la aereolina a utilizar: ",key="inputAereo")
                        precio = st.text_input("Ingrese el precio del boleto: ",key="inputPrecio")
                        alojamiento = st.text_input("Ingrese el lugar donde se va a alojar: ",key="inputAloj")
                        transporte = st.selectbox("Requiere de transporte: ",["...","Si","No"])  
                    
                    btnRegistrar = st.button("Registrar")
                    if btnRegistrar:
                        correo = st.session_state.user.getCorreo()
                        tipo = st.session_state.user.getTipo()
                        password = st.session_state.user.getPassword()
                        colaborador = Colaborador(correo,tipo,password, nombreCompleto, puesto, departamento)
                        viaje = Viaje(colaborador,viajeInternacional,pais,viaje,fechaInicio,fechaFin,aereolina,precio,alojamiento,transporte)
                        if encontrarColaborador(colaborador.generarDatosjson()):
                            try:
                                colaborador =  verificarDato(colaborador.generarDatosjson(),realizarConeccionUsuarios())
                                st.session_state.colaborador = Colaborador(colaborador["correo"],colaborador["password"],colaborador["tipo"],colaborador["informacion"]["nombre"],colaborador["informacion"]['puesto'],colaborador["informacion"]["departamento"])
                                res = insertarViaje(viaje.generarDatosJSON())
                                st.success(f"Viaje registrado efeactivamente para el colaborador {st.session_state.colaborador.getNombre()}")
                            except Exception as e:
                                print(e)
                                st.warning("No se ha completado el registro de los datos")

                        else:
                            try:
                                generarColaborador(st.session_state.user.generarDatosjson(),colaborador.generarDatosjson())
                                insertarViaje(viaje.generarDatosJSON())
                                st.success(f"Viaje registrado efeactivamente para el colaborador {colaborador.getNombre()}")
                                st.session_state.colaborador = colaborador
                            except Exception as e:
                                print(e)
                                st.warning("No se ha completado el registro de los datos")

        if accion=="Modificar/Eliminar una solicitud":
            modificar = st.container()
            with modificar:
                try:
                    viajesUsuario = [elem for elem in encontrarViajesUsuario(st.session_state.user)]
                    opcion = st.selectbox("Escoja el id de su solicitud",[elem["_id"] for elem in viajesUsuario])
                    st.write("Informacion actual de la solicitud: ")
                    columna1, columna2,columna3= st.columns(3)
                    st.write(viajesUsuario)
                    viajeSeleccionado = [elem for elem in viajesUsuario if elem["_id"]== opcion]
                    st.write(viajeSeleccionado)


                    with columna1:  
                        nuevoNombreCompleto = st.text_input('Ingrese su nombre completo:',value=viajeSeleccionado[0]["Colaborador"]["informacion"]["nombre"])
                        nuevoPuesto = st.text_input("Ingrese su puesto: ",value=viajeSeleccionado[0]["Colaborador"]["informacion"]["puesto"])
                        nuevoDepartamento = st.text_input("Ingrese el departamento en que trabaja: ",value=viajeSeleccionado[0]["Colaborador"]["informacion"]["departamento"])
                        nuevoViajeInternacional= st.selectbox("Su viaje es internacional: ", ["...","Si", "No"])
                        nuevoPais = st.text_input("Ingrese pais destino: ",value=viajeSeleccionado[0]["destino"])                        
                        nuevoViaje = st.selectbox("Motivo de viaje: ",["...","Seguimiento","Cierre venta", "Capacitacion"])

                    with columna3:
                        nuevaFechaInicio = st.date_input("Ingrese la fecha de inicio: ")
                        nuevaFechaFin = st.date_input("Ingrese la fecha de finalizacion: ")
                        st.subheader("Detalles del vuelo")
                        nuevaAereolina = st.text_input("Ingrese la aereolina a utilizar: ",value=viajeSeleccionado[0]["aerolinea"])
                        nuevoPrecio = st.text_input("Ingrese el precio del boleto: ",value=viajeSeleccionado[0]["precio"])
                        nuevoAlojamiento = st.text_input("Ingrese el lugar donde se va a alojar: ",value=viajeSeleccionado[0]["alojamiento"])
                        nuevoTransporte = st.selectbox("Requiere de transporte: ",["...","Si","No"])    

                        btnModificar = st.button("Modificar la informacion")
                        btnEliminar = st.button("Eliminar la solicitud")
                        if btnEliminar:
                            try:
                                eliminarViaje(viajeSeleccionado[0])
                                st.success(f"Viaje eliminado")
                            except Exception as e:
                                st.write(e)
                                st.warning(f"Viaje seleccionado no ha sido eliminado")

                        if btnModificar:
                            try:
                                colaboradorNuevo = Colaborador(st.session_state.user.getCorreo(), st.session_state.user.getTipo(),st.session_state.user.getPassword(),nuevoNombreCompleto,nuevoPuesto,nuevoDepartamento)
                                viaje = Viaje(colaboradorNuevo,nuevoViajeInternacional,nuevoPais,nuevoViaje,nuevaFechaInicio,nuevaFechaFin,nuevaAereolina,nuevoPrecio,nuevoAlojamiento,nuevoTransporte)
                                modificarViaje(viajeSeleccionado[0],viaje.generarDatosJSON())
                                st.success(f"Viaje modificado")
                            except Exception as e:
                                
                                st.warning(f"Fallo en la modificación de datos")
                except Exception:
                        st.warning("Debe registrar viajes para el colaborador")
                    
        if accion == "Ver solicitud de solicitudes":
            visualizacion = st.container()
            with visualizacion:
                    viajesUsuario = [elem for elem in encontrarViajesUsuario(st.session_state.user)]
                    opcion = st.selectbox("Escoja el id de su solicitud",[elem["_id"] for elem in viajesUsuario])
                    viajeSeleccionado = [elem for elem in viajesUsuario if elem["_id"]== opcion]
                    colaborador = viajeSeleccionado[0].pop("Colaborador")
                    viajeSeleccionado[0].pop("_id")
                    df = pd.DataFrame(viajeSeleccionado)
                    st.table(df)


if st.session_state.user and st.session_state.user.getTipo() == "Empleado":
    pantallaEmpleado = st.container()
    with pantallaEmpleado:
        st.title("Gestionar solicitudes")
        accion = st.selectbox("Seleccione su opcion: ",["...","Valorar solicitud","Consultar viajes programados","Consultar viajes internacionales","Consultar por destino especifico"])
        if accion == "Valorar solicitud":
            viajes = [elem for elem in encontrarViajesPendientes()]
            opcion = st.selectbox("Solicitudes en estado de pendiente: ",[elem["_id"] for elem in viajes])
            decision = st.selectbox("Desea aprobar o rechazar esta solicitud: ",["...","Aprobado","Rechazado"])
            viajeSeleccionado = [elem for elem in viajes if elem["_id"] == opcion]
            
            btnSolicitud = st.button("Actualizar solicitud")
            if btnSolicitud:
                try:
                    modificarViaje(viajeSeleccionado[0], {"estado": decision})
                    st.success(f"Estado modificado con éxito")
                except Exception:
                    st.warning("Fallo al actualizar la solicitud")


        if accion == "Consultar viajes programados":
            mes = st.selectbox("Ingrese el mes a consultar: ",[elem for elem in range(1,13)])
            año = st.selectbox("Ingrese el año a consultar: ",[elem for elem in range(1985,2028)])
            btnConsulta1 = st.button("Realizar consulta")
            if btnConsulta1:
                viajesProgramados = consultarViajesProgramados(mes, año)
                st.success(f"Consulta realizada con éxito")
                for elem in viajesProgramados:
                    elem.pop("Colaborador")
                    elem.pop("_id")
                df = pd.DataFrame(viajesProgramados)
                st.table(df)
            


        if accion == "Consultar viajes internacionales":
            trimestre = st.selectbox("Indique el trimestre que desea: ", ["1er Trimestre","2do Trimestre","3er Trimestre","4to Trimestre"])
            ano = st.selectbox("Indique el año del trimestre que desea consultar: ",[elem for elem in range(1985,2028)])

            btnConsulta2 = st.button("Realizar consulta")
            if btnConsulta2:
                try:
                    viajes = consultarViajesInternacional(trimestre,ano)
                    for elem in viajes:
                        elem.pop("Colaborador")
                        elem.pop("_id")
                    df = pd.DataFrame(viajes)
                    st.success(f"Consulta realizada con éxito")
                    st.table(df)
                except Exception as e:
                    st.write(e)
                    st.warning("Fallo en la consulta")

                    


            

        if accion == "Consultar por destino especifico":
            
            
            destino = st.selectbox("Seleccione un destino: ",[elem for elem in encontrarDestinos()])
            
            btnConsulta3 = st.button("Realizar consulta")
            if btnConsulta3:
                try:
                    viajes = [elem for elem in verificarDatos({"destino": destino},realizarConeccionViajes())]
                    for elem in viajes:
                        elem.pop("Colaborador")
                        elem.pop("_id")
                    df = pd.DataFrame(viajes)
                    st.table(df)
                    st.success(f"Consulta realizada con éxito")
                except Exception:
                    st.warning("No se ha completado la solicitud")

            
          
                        




            
