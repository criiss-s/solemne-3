import streamlit as st
import pandas as pd
import altair as alt
import base64

# Fondo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image_path = "fondo.jpg"
bg_image_base64 = get_base64_of_bin_file(bg_image_path)

page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_base64}");
        background-size: cover;
        background-position: center;  /* Centra la imagen */
    }}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.image("letras.png")
opcion = st.sidebar.selectbox('Selecciona una sección', ['Información', 'Campeones', 'Competitivo', 'Acerca de'])

st.image("League-of-Legends-logo.png")

# Cargar datos del CSV
@st.cache_data
def load_data():
    data = pd.read_csv('Champions_2024W(Hoja1).csv', encoding='latin1')
    return data

# Crear gráfico simple con Altair
def create_chart(data):
    chart = alt.Chart(data).mark_bar().encode(
        x='Campeón',
        y='Veces jugado'
    ).properties(
        width=600,
        height=400
    )
    return chart

# Análisis de Equipos
def mostrar_analisis_equipos():
    st.markdown("<h2 style='color: white;'>Análisis de Equipos</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color: white;'>Analiza el rendimiento de los equipos más destacados, su historial en torneos recientes y sus jugadores estrella.</p>
    """, unsafe_allow_html=True)
    # Datos de ejemplo
    equipos = pd.DataFrame({
        'Equipo': ['G2 Esports', 'T1', 'Fnatic', 'Gen.G', 'DAMWON Gaming'],
        'Partidas Jugadas': [20, 18, 22, 19, 21],
        'Victorias': [15, 14, 12, 16, 13],
        'Derrotas': [5, 4, 10, 3, 8]
    })
    st.table(equipos)

if opcion == 'Información':
    st.markdown("<h1 style='color: white;'>Información</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color: white;'>League of Legends es un videojuego multijugador de arena de batalla en línea desarrollado y publicado por Riot Games...</p>
    """, unsafe_allow_html=True)
elif opcion == 'Campeones':
    st.write('Aquí van los datos.')
elif opcion == 'Competitivo':
    st.markdown("<h1 style='color: white;'>Competitivo</h1>", unsafe_allow_html=True)
    video_url = "https://www.youtube.com/watch?v=Kv2rswmxBVs"
    st.video(video_url)
    st.markdown("""
    <div style="margin-left: -75px;">
        <h3 style="color: white;">¿Qué es el competitivo de League of Legends?</h3>
        <p style='color: white;'>El competitivo de League of Legends (LoL) se refiere a los torneos y ligas organizados por Riot Games...</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("17285869617624.jpg")
    
    # Añadir secciones adicionales
    mostrar_analisis_equipos()
    
    # Cargar los datos y crear el gráfico interactivo
    st.markdown("<h2 style='color: white;'>Estadísticas de Campeones</h2>", unsafe_allow_html=True)
    try:
        data = load_data()
        st.write("Datos cargados correctamente:")
        st.write(data.head())  # Muestra las primeras filas del DataFrame para inspección

        # Verificar nombres de columnas
        if 'Campeón' in data.columns and 'Veces jugado' in data.columns:
            chart = create_chart(data)
            st.altair_chart(chart, use_container_width=True)
        else:
            st.error("El archivo CSV no contiene las columnas 'Campeón' y 'Veces jugado'. Verifique el nombre de las columnas.")
    except Exception as e:
        st.error(f"Error al cargar los datos del CSV: {e}")

elif opcion == 'Acerca de':
    st.write('Aquí se mostraría la información adicional.')
