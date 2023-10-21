import streamlit as st

pantallaInicio1=st.container()
with pantallaInicio1:
    st.title("Sistema de Viajes")
    accion = st.selectbox("Seleccione su opcion: ",["...","Crear Cuenta","Iniciar Sesion"])
    if accion == "Iniciar Sesion":
        iniciarSesionC= st.container()
        with iniciarSesionC:
            cedula = st.text_input('Ingrese su usuario o cedula:',key="input_cedula")
            clave = st.text_input("Ingrese su contraseña: ",key="inputClave")
            btnIniciarSesion = st.button("Iniciar sesion")
            if btnIniciarSesion ==True:
                try:
                    usuario =  1
                except:
                    st.warning("cedula incorrecta")
    if accion  == "Crear Cuenta":
        crearCuenta=st.container()
        with crearCuenta:
            st.text('Por favor, agregue la informacion solicitada:')
            correo = st.text_input("Correo:",key="input_correo")
            contrasena = st.text_input("Contraseña:",key="input_contraseña")
            btnCrearCliente=st.button("Crear Cliente")
            btnContinuar= st.button("Continuar")
            if btnCrearCliente == True:
                try: 
                    st.warning("Se realizo la conexion")
                except:
                    st.warning("No se registro la informacion")
    
