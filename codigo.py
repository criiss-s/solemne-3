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
        <p style='color: white;'>El competitivo de League of Legends (LoL) se refiere a los torneos y ligas organizados por Riot Games donde equipos profesionales compiten por premios y reconocimiento. Estos torneos incluyen eventos regionales, nacionales e internacionales, como la League of Legends Championship Series (LCS), la League of Legends European Championship (LEC), y el Campeonato Mundial de League of Legends (Worlds), todo esto se realiza en amplios lugares para que asi los fanaticos de este juego puedan asistir de forma presencial y vivir una experiencia inolvidable.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Los Worlds de League of Legends son uno de los eventos de esports más conocidos debido a su audiencia global enorme, alta competitividad, prestigio histórico desde 2011, impresionante producción, participación de equipos icónicos como T1 y G2 Esports, accesibilidad gratuita en múltiples plataformas de streaming y el involucramiento activo de la comunidad con eventos adicionales y contenido exclusivo. Estos factores combinados hacen que sean uno de los eventos más esperados y seguidos en el mundo de los esports. En donde el ganador podra hacerse con la increible copa.
    </div>
    """, unsafe_allow_html=True)
    st.image("Copa Worlds.jpeg")

    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Rangos Competitivos</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Los rangos competitivos en League of Legends son una forma de clasificar a los jugadores según su habilidad y rendimiento en el juego. Estos rangos ayudan a emparejar a los jugadores con oponentes de habilidad similar para garantizar partidas justas y equilibradas. Aquí están los rangos competitivos de League of Legends, de menor a mayor:
    </div>
    """, unsafe_allow_html=True)
    st.image("Rangos Competitivos.png")
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Bronce es para jugadores que tienen un entendimiento básico del juego pero aún están desarrollando sus habilidades y estrategias. Plata es para jugadores promedio que tienen una buena comprensión del juego pero que todavía están trabajando en perfeccionar sus habilidades y tácticas. Oro es para jugadores por encima del promedio, con una comprensión sólida del juego y habilidades decentes. Este es un rango donde los jugadores comienzan a dominar las mecánicas básicas del juego. Platino es para jugadores habilidosos con una comprensión avanzada del juego y estrategias más refinadas. Aquí es donde los jugadores muestran un alto nivel de competencia. Esmeralda es un rango intermedio entre Platino y Diamante, reservado para jugadores que destacan pero no alcanzan el nivel de los mejores. Diamante es para jugadores altamente habilidosos, considerados entre los mejores del servidor. Estos jugadores tienen un gran conocimiento del juego y habilidades sobresalientes. Maestro es para jugadores de élite que están en la cima del competitivo. Tienen una comprensión profunda del juego y habilidades excepcionales. Gran Maestro es para jugadores que están justo debajo del nivel más alto, mostrando un nivel de competencia extremadamente alto y un dominio casi completo del juego. Challenger es para los mejores jugadores del servidor, en la cúspide del competitivo. Estos jugadores representan la élite absoluta y compiten al más alto nivel. Estos rangos ayudan a emparejar a los jugadores con oponentes de habilidad similar, creando partidas más justas y desafiantes. Cada rango está dividido en divisiones, excepto Maestro, Gran Maestro y Challenger, que no tienen divisiones
    </div>
    """, unsafe_allow_html=True)
    st.image("Tiers.jpg")

    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Videos</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    video_url = "https://www.youtube.com/watch?v=XSe08RXp1P8"
    st.video(video_url)
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">El mejor jugador de todos los tiempos</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Lee "Faker" Sang-hyeok es universalmente aclamado como el mejor jugador de League of Legends de todos los tiempos. Conocido como el "Rey Demonio Indomable", Faker ha dejado una marca indeleble en el competitivo de esports gracias a su destreza sin igual, su capacidad para realizar jugadas decisivas en momentos cruciales y su impresionante consistencia a lo largo de su carrera. Además de su éxito en torneos, Faker es conocido por su humildad y dedicación. Ha sido una fuente constante de inspiración para jugadores de todo el mundo, demostrando que el verdadero talento viene acompañado de una ética de trabajo inquebrantable y un deseo interminable de mejorar.El legado de Faker no solo se mide en títulos y premios, sino en el impacto duradero que ha tenido en la comunidad de esports. Ha elevado el estándar del juego competitivo y ha establecido un modelo a seguir para futuras generaciones de jugadores. Su nombre es sinónimo de excelencia, y su influencia seguirá siendo sentida mucho después de que se retire Faker es, sin lugar a dudas, el epítome de la grandeza en el mundo de los esports, y su historia es un testimonio del poder de la perseverancia, el talento y la pasión
    </div>
    """, unsafe_allow_html=True)


elif opcion == 'Acerca de':
    st.write('Aquí se mostraría la información adicional.')
    
    
    
    
    
