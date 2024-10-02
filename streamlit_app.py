import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Cargar credenciales desde el archivo JSON
creds = Credentials.from_service_account_file('credentials.json')

# Inicializar conexión con Google Sheets
gc = gspread.authorize(creds)

# Abrir la hoja de cálculo usando su ID
spreadsheet_id = '1prl2yPkqMDeUdA7Gi0NoSz6aqnORsRMDNou36yFbpbA'
worksheet_name = 'Registros de Usuarios'  # Cambia al nombre de tu hoja
worksheet = gc.open_by_key(spreadsheet_id).worksheet(worksheet_name)

# Leer datos existentes
existing_data = pd.DataFrame(worksheet.get_all_records())
existing_data = existing_data.dropna(how='all')

# Formulario para agregar nuevos registros
with st.form(key='user_form'):
    celular = st.text_input(label='Celular*')
    contrasena = st.text_input(label='Contraseña*', type='password')
    
    submit_button = st.form_submit_button(label='Registrar Usuario')
    
    if submit_button:
        if not celular or not contrasena:
            st.warning('Por favor, complete todos los campos obligatorios.')
            st.stop()
        elif existing_data['celular'].str.contains(celular).any():
            st.warning('El número de celular ya está registrado.')
            st.stop()
        else:
            # Crear una nueva fila de datos
            new_user_data = {
                'celular': celular,
                'contrasena': contrasena
            }
            # Agregar el nuevo usuario a la hoja
            worksheet.append_row(list(new_user_data.values()))
            st.success('Usuario registrado con éxito.')

# Mostrar datos existentes
if not existing_data.empty:
    st.subheader('Usuarios Registrados')
    st.dataframe(existing_data)
