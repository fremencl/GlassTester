#import requests
import streamlit as st

# Ruta a los archivos de imagen en tu carpeta 'lottiefiles'
ruta_imagen = "./lottiefiles/Octica.png"

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
    st.header("Mira la Cámara")
    foto = st.camera_input("Tomemos una linda foto")
    if foto:
        st.success("¡Tu foto se cargó correctamente!")
        # Aquí puedes agregar código adicional para procesar la foto si es necesario

with st.container():
    st.write("--")
    st.header("Te gustó como te ves con estos lentes?")
    text_column, image_column = st.columns((1, 2))  # Asegúrate de que las columnas estén en el orden correcto
    with text_column:
        st.write("ECONOPTICA - Somos tu óptica en línea con los mejores precios")
        st.markdown("[Nuestra Tienda web...](https:///juguetesingenium.cl)")
    with image_column:
        st.image(ruta_imagen, use_column_width=True)
