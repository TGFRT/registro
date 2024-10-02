import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Cargar las credenciales desde los secretos de Streamlit
secrets = st.secrets["gcp"]

# Crear las credenciales
creds = Credentials.from_service_account_info({
    "type": "service_account",
    "private_key": secrets["private_key"],
    "client_email": secrets["client_email"]
})

# Inicializar la conexión con Google Sheets
gc = gspread.authorize(creds)

# Abrir la hoja de cálculo usando el ID
spreadsheet_id = "TU_SPREADSHEET_ID"  # Reemplaza con tu ID
spreadsheet = gc.open_by_key(spreadsheet_id)
worksheet = spreadsheet.sheet1  # O usa el nombre de la hoja

# Aquí puedes agregar el resto de tu lógica de Streamlit
st.title("Mi Aplicación de Google Sheets")
data = worksheet.get_all_records()
st.write(data)
