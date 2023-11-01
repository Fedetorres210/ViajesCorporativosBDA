import streamlit as st
import subprocess
from  logica.Clases import Usuario, Viaje,Colaborador
from config.config import insertarValor, verificarInicioSesion,verificarDato


if 'btnIniciarSesionClicked' not in st.session_state:
    st.session_state.btnIniciarSesionClicked = False




pantallaInicio1=st.container()
with pantallaInicio1:
    st.title("Sistema de Viajes")
    accion = st.selectbox("Seleccione su opcion: ",["...","Crear Cuenta","Iniciar Sesion"])
    if accion == "Iniciar Sesion":
        iniciarSesionC= st.container()
        with iniciarSesionC:
            correo = st.text_input('Ingrese su usuario o cedula:',key="input_cedula")
            clave = st.text_input("Ingrese su contraseña: ",key="inputClave")
            btnIniciarSesion = st.button("Iniciar sesion")
            if btnIniciarSesion:
                st.session_state.btnIniciarSesionClicked = not st.session_state.btnIniciarSesionClicked
                if st.session_state.btnIniciarSesionClicked:
                    e = Exception("Error al encontrar el usuario revise el Correo, la contraseña o la conexion con base de datos ")
                            
                    try:
                        filtro = {"correo":correo, "password":clave}
                        usuarioActual = verificarDato(filtro)
                        usuarioActual = Usuario(usuarioActual['correo'], usuarioActual['password'],usuarioActual['tipo'])
                        if(verificarInicioSesion(filtro)):
                            st.success(f"Bienvenido de regreso {usuarioActual.getTipo()}")
                            if(usuarioActual.getTipo() == "Colaborador"):
                                pantallaEmpleado=st.container()
                                with pantallaEmpleado:
                                    st.title("Gestionar solicitudes")
                                    accion = st.selectbox("Seleccione su opcion: ",["...","Valorar solicitud","Consultar viajes programados","Consultar viajes internacionales","Consultar por destino especifico"])
                                    if accion == "Valorar solicitud":
                                        opcion = st.selectbox("Solicitudes en estado de pendiente: ",["AQUI VAN LAS SOLICITUDES GENERADAS EN UN FOR"])
                                        decision = st.selectbox("Desea aprobar o rechazar esta solicitud: ",["...","Aprobar","Rechazar"])
                                    if accion == "Consultar viajes programados":
                                        #CONSULTA
                                        fecha = st.date_input("Ingrese la fecha a consultar: ")
                                        st.table(["Hola"])
                                    if accion == "Consultar viajes internacionales":
                                        st.selectbox("Indique el trimestre que desea: ", ["1er Trimestre","2do Trimestre","3er Trimestre","4to Trimestre"])
                                        st.text_input("Indique el año del trimestre que desea consultar: ")

                                        #CONSULTA
                                        st.table(["Hola 2.0"])
                                    if accion == "Consultar por destino especifico":
                                        destino = st.selectbox("Seleccione un destino: ",['DROPDOWN'])
                                        st.table(["Hola"])
                            

                        
                    except:
                        st.error(e)




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
                    print(tipo)
                    miUsuario = Usuario(correo,contrasena,tipo)
                    print(miUsuario)
                    print(miUsuario.generarDatosjson())
                    res = insertarValor(miUsuario.generarDatosjson())
                    
                    if(res):
                        st.success("Se registro con exito la conexion")
                    else:
                        raise (Exception("Fallo en la conexion con la base de datos "))
                   
                except:
                    st.warning("No se registro la informacion")



   

   
          
                        




            
