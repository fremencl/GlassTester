import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

#Funcion para nuestra animacion
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

lottie_coding = load_lottieurl("https://lottie.host/embed/3d1e0c61-ff21-4eb8-bf49-23aeae2609d0/sRiDPU44t3.json")
imagen_video = Image.open("/content/Octica.png")

with st.container():
  st.subheader("Llegó el momento de probar tus lentes")
  st.title("Tomemos una foto y veamos como te luce este modelo")
  st.write("XXXXXXXX")

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("Mira la Cámara")
    #st.write(
      #"""
        #Texto aquí
      #"""
    #)
  with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
  st.write("--")
  st.header("Te gustó como te ves con estos lentes?")
    image_column, text_column = st.columns((1, 2))
  with image_column:
    st.image(imagen_video)
  with text_column:
    st.write(
      """
      ECONOPTICA - Somos tu optica en linea con los mejores precios
      """
    )
    st.markdown("[Nuestra Tienda web...](https:///juguetesingenium.cl)")
