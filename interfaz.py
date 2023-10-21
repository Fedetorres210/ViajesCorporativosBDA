import streamlit as st
from  logica.Clases import Usuario, Viaje,Colaborador
from config.config import insertarValor, verificarInicioSesion

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
                e = Exception("Error al encontrar el usuario revise el Correo, la contraseña o la conexion con base de datos ")
                        
                try:
                    miUsuario = Usuario(correo,clave)
                    if(verificarInicioSesion(miUsuario.generarDatosjson())):
                        st.success(f"Bienvenido de regreso {miUsuario.getCorreo()}")
                    else:
                        raise e
                except:
                    st.error(e)




    if accion  == "Crear Cuenta":
        crearCuenta=st.container()
        with crearCuenta:
            st.text('Por favor, agregue la informacion solicitada:')
            correo = st.text_input("Correo:",key="input_correo")
            contrasena = st.text_input("Contraseña:",key="input_contraseña")
            btnCrearCliente=st.button("Crear Cliente")
            ##POR ALLA ME VOLARIA EL BOTON CONTINUAR 
            btnContinuar= st.button("Continuar")
            if btnCrearCliente:
                try: 
                    
                    miUsuario = Usuario(correo,contrasena)
                    print(miUsuario.generarDatosjson())
                    res = insertarValor(miUsuario.generarDatosjson())
                    
                    if(res):
                        st.success("Se registro con exito la conexion")
                    else:
                        raise (Exception("Fallo en la conexion con la base de datos "))
                   
                except:
                    st.warning("No se registro la informacion")
    
