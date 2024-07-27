import streamlit as st  

# Título de la página
st.title("Bienvenido a esta página para procesar imágenes.🖼️")

# Breve descripción
st.write("En esta página podrás escoger una imagen de tu galeria de fotos y "
         "modificarla a tu gusto con las opciones que tenemos preparadas para ti.")

opcion = st.radio("¿Listo?", ("Nada", "Sí", "No"))
if opcion == "Sí":
    nombre = st.text_input("¿Cómo te llamas?")

    if nombre:
        st.write(f"¡Buenas {nombre}😉!, escoge la imagen que deseas modificar:")

        # Subir imagen  
        ima = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])
        
elif opcion == "No":
    st.text("Lamentamos no poder ayudarte.😪")