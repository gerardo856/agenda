import streamlit as st
import pandas as pd
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Función para autenticar y obtener acceso a Google Sheets
def autenticar_google_sheets():
    # Define el alcance de la API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    # Usar el archivo de credenciales JSON descargado (ajusta la ruta al archivo correcto)
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)  # Ajusta la ruta a tu archivo JSON
    cliente = gspread.authorize(creds)
    
    # Abrir la hoja de Google Sheets por su nombre y seleccionar la hoja "Hoja 1"
    hoja = cliente.open("agenda").worksheet("Hoja 1")
    return hoja

# Título de la aplicación
st.title("Agendar una Cita")

# Descripción
st.write("""
    Bienvenido a la aplicación de agendamiento de citas. Aquí puedes seleccionar una fecha y hora para reservar tu cita.
    """)

# Obtener la fecha actual para mostrar las opciones disponibles
hoy = datetime.date.today()

# Crear un calendario interactivo con Streamlit
fecha_seleccionada = st.date_input("Selecciona la fecha para tu cita:", min_value=hoy)

# Si la fecha seleccionada es válida, mostrar la hora disponible
if fecha_seleccionada >= hoy:
    horas_disponibles = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    
    hora_seleccionada = st.selectbox("Selecciona la hora para tu cita:", horas_disponibles)

    # Crear botón de agendar cita
    if st.button("Agendar cita"):
        # Mostrar mensaje de éxito
        st.success(f"¡Cita agendada para el {fecha_seleccionada} a las {hora_seleccionada}!")

        # Autenticación y acceso a Google Sheets
        hoja = autenticar_google_sheets()

        # Guardar la cita en Google Sheets (en la hoja "Hoja 1")
        nueva_cita = [str(fecha_seleccionada), hora_seleccionada]
        hoja.append_row(nueva_cita)  # Añadir una nueva fila al final de la hoja

        st.write("Tu cita ha sido guardada exitosamente en Google Sheets.")
else:
    st.warning("Por favor selecciona una fecha válida para agendar tu cita.")
