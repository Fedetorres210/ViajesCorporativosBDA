import streamlit as st

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

        



         
