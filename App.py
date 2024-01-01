import json
import time

import requests
import streamlit as st
#from streamlit_lottie import st_lottie
#from streamlit_lottie import st_lottie_spinner

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Rutas a los archivos Lottie y de imagen en tu carpeta 'lottiefiles'
lottie_lentes = load_lottiefile("./lottiefiles/animalentes.json")
url_imagen = "./lottiefiles/octica.png"

st.set_page_config(
    page_title="Optica Digital",
    page_icon=":tada:",
)

st.title("Llegó el momento de probar tus lentes!")
st.markdown(
    """
Ahora puedes ver cómo te quedarán este modelo de lentes, si no te gustan no es problema, puedes elegir otro modelo y probártelo digitalmente. La idea es que encuentres el modelo que mejor luce en ti.
"""
)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Mira la Cámara")
    with right_column:
        st_lottie(lottie_lentes, height=300, key="lentes")

with st.container():
    st.write("--")
    st.header("Te gustó como te ves con estos lentes?")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(url_imagen, use_column_width=True)
    with text_column:
        st.write(
            """
            ECONOPTICA - Somos tu óptica en línea con los mejores precios
            """
        )
        st.markdown("[Nuestra Tienda web...](https:///juguetesingenium.cl)")
