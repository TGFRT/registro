import streamlit as st

# Accede a los secretos
google_secrets = st.secrets["google"]

# Usa las credenciales
from google.oauth2 import service_account
import gspread

credentials = service_account.Credentials.from_service_account_info(google_secrets)
gc = gspread.authorize(credentials)

# Ahora puedes usar `gc` para interactuar con Google Sheets
spreadsheet_id = '1prl2yPkqMDeUdA7Gi0NoSz6aqnORsRMDNou36yFbpbA'
spreadsheet = gc.open_by_key(spreadsheet_id)
