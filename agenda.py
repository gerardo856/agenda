import streamlit as st
import pandas as pd
import datetime

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
        st.success(f"¡Cita agendada para el {fecha_seleccionada} a las {hora_seleccionada}!")
        
        # Guardar la cita en un archivo (por ejemplo, en un CSV)
        cita = pd.DataFrame({
            'Fecha': [fecha_seleccionada],
            'Hora': [hora_seleccionada]
        })
        
        # Guardar el archivo CSV
        cita.to_csv("citas_agendadas.csv", mode='a', header=False, index=False)
        st.write("Tu cita ha sido guardada exitosamente.")
else:
    st.warning("Por favor selecciona una fecha válida para agendar tu cita.")
