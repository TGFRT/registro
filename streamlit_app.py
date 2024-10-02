import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import toml

# Cargar las credenciales desde secrets.toml
secrets = toml.load("secrets.toml")
google_creds = secrets['google']

# Configura las credenciales
creds = Credentials.from_service_account_info(google_creds)

# Autenticación con Google Sheets
gc = gspread.authorize(creds)

# ID de la hoja de cálculo
spreadsheet_id = '1prl2yPkqMDeUdA7Gi0NoSz6aqnORsRMDNou36yFbpbA'

# Abre la hoja de cálculo por su ID
spreadsheet = gc.open_by_key(spreadsheet_id)

# Selecciona la primera hoja
worksheet = spreadsheet.sheet1  # Puedes cambiar esto si necesitas otra hoja

# Lee datos de la hoja
data = worksheet.get_all_records()

# Muestra los datos en Streamlit
st.title("Registros de Usuarios")
st.write(data)
