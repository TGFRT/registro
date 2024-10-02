import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Credenciales directamente integradas
secrets = {
    "type": "service_account",
    "project_id": "login-437414",
    "private_key_id": "c306e0c35281bfc8efa51fb01d8a0bafaa349658",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCly6+2DxdXCeV4\niJRO1UXpA5BIzDO3ekkQDTBjgJZoOXELOSrbUR4VhunvRMZGwiWawgZ6RG9XMuKA\nkVSZy3UTUJ88sk0mrryIu8qkPSwvGvyo7TdFmZAgW6b7VKO9hYYk/43YqKfB5hnn\nky4oqj0A2K5ydKNfhJny+trvkQhcFIePfIdTDY+kD2lgwakpCYTtwtvMoE1U/jld\n6hDX94uLJ1hVbJvsyI2FPZXFm2d6e42NZF5SJlGlOE8EE2VieatJKonbOIPhCHOj\nhsFBwYAUAaoI1o7AjR1rFa+cSvQ0ZpHz2Gs6s/08/mOFNEEO2KFQRJOKiBBwLp9x\npQspC2bXAgMBAAECggEAOd3f1DFsOgrQNsOkz+cMYYnG4EG1g0KBIcMYsoH8/R+f\nXwVy+d1UHLtcBxEAC05UBbHWxPIB0nOGLs2Ks6sZj8ZB7dNlriyqzSaOUciwFTjc\nGrHA6t/wN/sFSw99nvZtnZg8j/Q9qSWAwRzTrYnNhPAb4wLmyr3jZbU8mQUL3+cR\nfz2au7e6nSt4VNf4XPZUDA1RtzCSq3mxS89SVOtjnxu2IHOtqXs7CK406iKng4Ym\nTFa2/VOKGQykqFJ2yuVP+2zXrMhx37XUSWpPS3gzM4L4a6OLIZYdvaeHMDrCKVxK\nUqH0PqVqSWrntdPI6GnBkC3A1UGdHXXPItDdngevAQKBgQDpjbIYBgGOKBixq3hX\nwv9TBZZEbseDCd+AwGBQsUVtYRqIwm6L6vvuZa/z1qCJpmoifczzck9sbsXkivPG\nuIAqBoN+p2J5TbbmCgaO2tzzBaZ7s6HpD73Ucgc6rFZuYCCfk2FYNzXGb7DDsWQS\nSaNlYaOnSJO1tMURMWd/qw7xFwKBgQC1uuPRZJyN/2vJ8nq/5TzK8Ei63HHT5Tnu\nS+vELW+zMB+ZYcX33VlXQDgh1DbQPVdkGBu2IJEK/UsolnSqIahxyP0vfYVuVkJ9\nM3Kf4c5iQxb6r/LgO7UryZEfR0YVdnV+LHzRJ5n1i3XEhzM+aghVRV9OOAibebqT\nxc18//9QQQKBgDpCWlabyO+JGP/Y4iAiSEaRcjaH28TYRaR8WIpIbiUmv9O1jJXi\nfA2v2ABfXZR4qqkH8IQZ064cw8iK0NyVUYMqNMr3Ph08QY+ImLIx7kPA+RKKcK0O\nfC/ucdc0/ipyWDD2NqYmv4dMfS+TpH7bV6MGhChKdm4xNadgR40VQpjpAoGAe1Ik\nsP6egnm28qbah4gPNgPSxwM7NzjRlBTvHARdTXK1rsc7qVULAHty2/n/bFaEDEeT\n3obBBn0WWKeo6Z7HiNeEgIqkVliw6/dSrI52GBZA7MMjhOjfq6QwF9KtC3mEh6e2\n19QQ1SDbPQ8mRg98MilOYG0D4kW7x/Wt2Up7PkECgYEAnZkx2/aL+n/jyGIvZaAb\nhCHkzqonROJvbytWC0KL6Va2ULlW28znfYUbVFxsTz6LV5T2JgqpCFG0P1Z2XTJt\nsDN+CYNM7Hdswg6bQxy+dHoBBkYdhtGcA2SUqcmR7ynQgj25XdtuDSWE9+Ptpbay\nMgIlw0G0gUb0EljtMUA6tpM=\n-----END PRIVATE KEY-----\n",
    "client_email": "prueba@login-437414.iam.gserviceaccount.com",
    "client_id": "111792439871437679331",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/prueba%40login-437414.iam.gserviceaccount.com",
}

# Configurar los ámbitos y las credenciales
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(secrets, scopes=SCOPES)

# Inicializar la conexión con Google Sheets
gc = gspread.authorize(creds)

# Abrir la hoja de cálculo usando el ID
spreadsheet_id = "1prl2yPkqMDeUdA7Gi0NoSz6aqnORsRMDNou36yFbpbA"
worksheet_name = "Registros de Usuarios"  # Nombre de la hoja
spreadsheet = gc.open_by_key(spreadsheet_id)
worksheet = spreadsheet.worksheet(worksheet_name)

# Leer los datos existentes
existing_data = pd.DataFrame(worksheet.get_all_records())
existing_data = existing_data.dropna(how="all")

# Formulario para agregar nuevos registros
with st.form(key="user_form"):
    celular = st.text_input(label="Celular*")
    contrasena = st.text_input(label="Contraseña*", type="password")
    
    # Marcar campos obligatorios
    st.markdown("**Campos obligatorios***")
    
    submit_button = st.form_submit_button(label="Registrar Usuario")
    
    if submit_button:
        if not celular or not contrasena:
            st.warning("Por favor, complete todos los campos obligatorios.")
            st.stop()
        elif existing_data["celular"].str.contains(celular).any():
            st.warning("El número de celular ya está registrado.")
            st.stop()
        else:
            # Crear una nueva fila de datos
            new_user_data = {
                "celular": celular,
                "contrasena": contrasena
            }
            
            # Agregar el nuevo usuario a la hoja
            worksheet.append_row(list(new_user_data.values()))
            st.success("Usuario registrado con éxito.")

# Mostrar datos existentes
if not existing_data.empty:
    st.subheader("Usuarios Registrados")
    st.dataframe(existing_data)
