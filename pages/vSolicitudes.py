import streamlit as st
from  logica.Clases import Usuario, Viaje,Colaborador

pantallaSolicitudd=st.container()
with pantallaSolicitudd:
    st.title("Solicitudes")
    accion = st.selectbox("Seleccione su opcion: ",["...","Registro de una solicitud de viaje","Modificar/Eliminar una solicitud","Ver solicitud de solicitudes"])
    if accion == "Registro de una solicitud de viaje":
       registro= st.container()
       with registro:
            columna1, columna2,columna3= st.columns(3)
            with columna1:    
                nombreCompleto = st.text_input('Ingrese su nombre completo:',key="input_nombreCompleto")
                puesto = st.text_input("Ingrese su puesto: ",key="inputPuesto")
                departamento = st.text_input("Ingrese el departamento en que trabaja: ",key="inputDepartamento")
                viajeInternacional= st.selectbox("Su viaje es internacional: ", ["...","Si", "No"])
                pais = st.text_input("Ingrese pais destino: ",key="inputpais")
                viaje = st.selectbox("Motivo de viaje: ",["...","Seguimiento","Cierre venta", "Capacitacion"])
            with columna3:
                fechaInicio = st.date_input("Ingrese la fecha de inicio: ")
                fechaFin = st.date_input("Ingrese la fecha de finalizacion: ")
                st.text("Detalles del vuelo")
                aereolina = st.text_input("Ingrese la aereolina a utilizar: ",key="inputAereo")
                precio = st.text_input("Ingrese el precio del boleto: ",key="inputPrecio")
                alojamiento = st.text_input("Ingrese el lugar donde se va a alojar: ",key="inputAloj")
                transporte = st.selectbox("Requiere de transporte: ",["...","Si","No"])  
            #FALTA GENERAR EL ID  
            btnRegistrar = st.button("Registrar")

    if accion=="Modificar/Eliminar una solicitud":
        modificar = st.container()
        with modificar:
            opcion = st.selectbox("Escoja el id de su solicitud",["AQUI VAN LAS SOLICITUDES GENERADAS EN UN FOR"])
            st.write("Informacion actual de la solicitud: ")
            columna1, columna2,columna3= st.columns(3)
            with columna1:  
                nuevoNombreCompleto = st.text_input('Ingrese su nombre completo:',value="AQUI VA EL DROPDOWN")
                nuevoPuesto = st.text_input("Ingrese su puesto: ",value="AQUI VA EL DROPDOWN")
                nuevoDepartamento = st.text_input("Ingrese el departamento en que trabaja: ",value="AQUI VA EL DROPDOWN")
                nuevoViajeInternacional= st.selectbox("Su viaje es internacional: ", ["...","Si", "No"])
                nuevoPais = st.text_input("Ingrese pais destino: ",value="AQUI VA EL DROPDOWN")
                nuevoViaje = st.selectbox("Motivo de viaje: ",["...","Seguimiento","Cierre venta", "Capacitacion"])
            with columna3:
                nuevaFechaInicio = st.date_input("Ingrese la fecha de inicio: ")
                nuevaFechaFin = st.date_input("Ingrese la fecha de finalizacion: ")
                st.text("Detalles del vuelo")
                nuevaAereolina = st.text_input("Ingrese la aereolina a utilizar: ",value="AQUI VA EL DROPDOWN")
                nuevoPrecio = st.text_input("Ingrese el precio del boleto: ",value="AQUI VA EL DROPDOWN")
                nuevoAlojamiento = st.text_input("Ingrese el lugar donde se va a alojar: ",value="AQUI VA EL DROPDOWN")
                nuevoTransporte = st.selectbox("Requiere de transporte: ",["...","Si","No"])    
            btnModificar = st.button("Modificar la informacion")
            btnEliminar = st.button("Eliminar la solicitud")

    if accion == "Ver solicitud de solicitudes":
        visualizacion = st.container()
        with visualizacion:
            opcion = st.selectbox("Escoja el id de su solicitud",["AQUI VAN LAS SOLICITUDES GENERADAS EN UN FOR"])
            columna1, columna2,columna3= st.columns(3)
            with columna1:    
                nombreCompleto = st.text_input('Nombre completo:',value="AQUI VA EL DROPDOWN")
                puesto = st.text_input("Puesto: ",value="AQUI VA EL DROPDOWN")
                departamento = st.text_input("Departamento en que trabaja: ",value="AQUI VA EL DROPDOWN")
                viajeInternacional= st.text_input("Su viaje es internacional: ",value="AQUI VA EL DROPDOWN")
                pais = st.text_input("Pais destino: ",value="AQUI VA EL DROPDOWN")
                viaje = st.text_input("Motivo de viaje: ",value="AQUI VA EL DROPDOWN")
                estado = st.text_input("Estado: ",value="AQUI VA EL DROPDOWN")
            with columna3:
                fechaInicio = st.text_input("Fecha de inicio: ",value="AQUI VA EL DROPDOWN")
                fechaFin = st.text_input("Fecha de finalizacion: ",value="AQUI VA EL DROPDOWN")
                st.text("Detalles del vuelo")
                aereolina = st.text_input("Aereolina a utilizar: ",value="AQUI VA EL DROPDOWN")
                precio = st.text_input("Precio del boleto: ",value="AQUI VA EL DROPDOWN")
                alojamiento = st.text_input("Lugar donde se va a alojar: ",value="AQUI VA EL DROPDOWN")
                transporte = st.text_input("Requiere de transporte: ",value="AQUI VA EL DROPDOWN")  
                