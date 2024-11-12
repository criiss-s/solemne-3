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
     <p style='color: white;'>Características principales del competitivo de LoL:
Ligas profesionales: Existen ligas regionales en todo el mundo, como la LCS (Liga de Campeones de América del Norte), la LEC (Liga Europea de Campeones), la LCK (Liga Coreana de Campeones) y la LPL (Liga China de Campeones). Estas ligas son de gran prestigio y agrupan a los mejores equipos de cada región.

Torneos internacionales: El evento más importante es el Campeonato Mundial de LoL (World Championship o Worlds), que reúne a los mejores equipos de todas las ligas regionales. Además, existe el Mid-Season Invitational (MSI), que reúne a los campeones de cada región para competir en una serie de enfrentamientos a mitad de temporada.

Formato de competencia: Los equipos compiten en un formato de liga, donde se enfrentan a otros equipos a lo largo de varias semanas. Los mejores equipos avanzan a playoffs, donde compiten por el campeonato de su liga o por un lugar en torneos internacionales.

Equipos y jugadores: Los equipos en el competitivo de LoL están formados por cinco jugadores, cada uno especializado en un rol específico (top, jungla, mid, bot y support). Además, los entrenadores y el personal de análisis de datos juegan un papel fundamental para el rendimiento del equipo.

Aspectos técnicos y estratégicos: Las partidas competitivas de LoL son muy tácticas. Los equipos deben coordinarse bien, gestionar recursos como el oro y los objetos, tomar decisiones en tiempo real y ejecutar estrategias complejas. Los cambios en los parches (actualizaciones del juego) y las selecciones de campeones son elementos cruciales en cada enfrentamiento.

Aficionados y transmisiones: Los partidos de LoL son transmitidos en plataformas como Twitch, YouTube y loL Esports, donde los aficionados pueden ver los partidos en vivo, seguir análisis y comentar en tiempo real.

Cultura de esports: La escena competitiva de LoL ha generado una enorme comunidad global de jugadores, aficionados, creadores de contenido y patrocinadores. Los jugadores profesionales son considerados figuras públicas dentro del mundo de los deportes electrónicos, con gran cantidad de seguidores en redes sociales.</p>
    """, unsafe_allow_html=True)
elif opcion == 'Acerca de':
    st.write('Aquí se mostraría la información adicional.')





