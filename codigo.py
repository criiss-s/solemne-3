import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64


#fondo
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



if opcion == 'Información':
    st.markdown("<h1 style='color: white;'>Información</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color: white;'>League of Legends es un videojuego multijugador de arena de batalla en línea desarrollado y publicado por Riot Games. Inspirándose en Defense of the Ancients, un mapa personalizado para Warcraft III, los fundadores de Riot buscaron desarrollar un juego independiente del mismo género. Desde su lanzamiento en octubre de 2009, LoL ha sido un juego gratuito y se monetiza a través de la compra de elementos para la personalización de personajes y otros accesorios. El juego está disponible para Microsoft Windows y macOS.</p>
    """, unsafe_allow_html=True)
elif opcion == 'Campeones':
    st.write('Aquí van los datos.')
elif opcion == 'Competitivo':
    st.markdown("<h1 style='color: white;'>Competitivo</h1>", unsafe_allow_html=True)
    video_url = "https://www.youtube.com/watch?v=Kv2rswmxBVs"
    st.video(video_url)
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">¿Que es el competitivo de league of legends?</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>El competitivo de League of Legends (LoL) se refiere a los torneos y ligas organizados por Riot Games donde equipos profesionales compiten por premios y reconocimiento. Estos torneos incluyen eventos regionales, nacionales e internacionales, como la League of Legends Championship Series (LCS), la League of Legends European Championship (LEC), y el Campeonato Mundial de League of Legends (Worlds)p>
    </div>
    """, unsafe_allow_html=True)
    st.image("Equipos worlds1080x1350.jpg", width=100)
    
    
elif opcion == 'Acerca de':
    st.write('Aquí se mostraría la información adicional.')





