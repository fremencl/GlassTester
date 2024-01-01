import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Función para cargar la animación Lottie desde una URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URL de la imagen
url_imagen = "https://i.postimg.cc/Kcd2DR4s/Bit-Logo-Solo-2.png"

# URL de la animación Lottie
url_lottie = "https://lottie.host/embed/3d1e0c61-ff21-4eb8-bf49-23aeae2609d0/sRiDPU44t3.json"

# Encabezado y título
st.subheader("Llegó el momento de probar tus lentes")
st.title("Tomemos una foto y veamos cómo te luce este modelo")

# Lottie
lottie_coding = load_lottieurl(url_lottie)
st_lottie(lottie_coding, height=300, key="coding")

# Te gustó como te ves con estos lentes?
st.header("¿Te gustó cómo te ves con estos lentes?")

# Mostrar la imagen desde la URL
st.image(url_imagen, use_column_width=True)

# Texto adicional
st.write("ECONOPTICA - Somos tu óptica en línea con los mejores precios")
st.markdown("[Nuestra Tienda web...](https://juguetesingenium.cl)")
