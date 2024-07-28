import streamlit as st  
from PIL import Image  
import numpy as np  
import cv2  


# Funciones de procesamiento de imágenes  
def escala_grises(image):  
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  


def detectar_bordes(image):  
    return cv2.Canny(image, 100, 200)  


def rotar(image, angle):  
    height, width = image.shape[:2]  
    center = (width // 2, height // 2)  
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)  
    return cv2.warpAffine(image, matrix, (width, height))  


def redimensionar(image, scale_percent):  
    width = int(image.shape[1] * scale_percent / 100)  
    height = int(image.shape[0] * scale_percent / 100)  
    return cv2.resize(image, (width, height))  


def invertir_colores(image):  
    return cv2.bitwise_not(image)   


# Título de la página  
st.title("Bienvenido a esta página para procesar imágenes.🖼️")  

# Breve descripción  
st.write("En esta página podrás escoger una imagen de tu galería y modificarla"  
         " a tu gusto con las opciones que tenemos preparadas para ti😉.")  

# Reiniciar valores en la sesión   
if st.button("Reiniciar Página"):  
    st.session_state.clear()  # Limpia los estados de la sesión  
    st.experimental_rerun()  # Reinicia la aplicación  

# Mostrar el estado actual del botón de reinicio  
opcion = st.radio("¿Listo?", ("Nada", "Sí", "No"))  
if opcion == "Sí":  
    nombre = st.text_input("¿Cómo te llamas?")  
    if nombre:  
        st.write(f"¡Buenas {nombre}😉!, escoge la imagen que deseas modificar:")  

        # Subir imagen  
        ima = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])  

        if ima is not None:  
            # Leer la imagen usando PIL  
            image = Image.open(ima)  

            # Obtener el formato de la imagen  
            formato = ima.type  
            st.write(f"{nombre}, el formato de la imagen que has elegido es: {formato}")  

            # Convertir imagen a un formato que OpenCV puede procesar  
            image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  

            # Mostrar la imagen cargada al inicio  
            st.subheader("Imagen Cargada")  
            st.image(image, caption="Imagen Original", use_column_width=True)  

            # Variable para guardar la imagen procesada  
            procesada = {}  

            # Menú de operaciones  
            st.sidebar.subheader("Opciones de Procesamiento👌")  
            operaciones = ["Escala de Grises", "Detección de Bordes", "Rotar Imagen",   
                        "Redimensionar Imagen", "Invertir Colores"]  
            for operacion in operaciones:  
                if st.sidebar.checkbox(operacion):  
                    if operacion == "Escala de Grises":  
                        procesada[operacion] = escala_grises(image_cv)  
                        st.subheader("Imagen en Escala de Grises")  
                        st.image(procesada[operacion], caption="Imagen en Escala de Grises", channels="GRAY", use_column_width=True)  

                    elif operacion == "Detección de Bordes":  
                        procesada[operacion] = detectar_bordes(image_cv)  
                        st.subheader("Detección de Bordes")  
                        st.image(procesada[operacion], caption="Bordes Detectados", channels="GRAY", use_column_width=True)  

                    elif operacion == "Rotar Imagen":  
                        angulo = st.sidebar.slider("Selecciona el ángulo de rotación", -180, 180, 0)  
                        procesada[operacion] = rotar(image_cv, angulo)  
                        st.subheader("Imagen Rotada")  
                        st.image(procesada[operacion], caption=f"Imagen Rotada a {angulo}°", use_column_width=True)  
  
                    elif operacion == "Redimensionar Imagen":  
                        escala = st.sidebar.slider("Selecciona el porcentaje de escalado", 10, 200, 100)  
                        procesada[operacion] = redimensionar(image_cv, escala)  
                        st.subheader("Imagen Redimensionada")  
                        st.image(procesada[operacion], caption=f"Imagen Redimensionada al {escala}%", use_column_width=True)  

                    elif operacion == "Invertir Colores":  
                        procesada[operacion] = invertir_colores(image_cv)  
                        st.subheader("Imagen con Colores Invertidos")  
                        st.image(procesada[operacion], caption="Imagen con Colores Invertidos", use_column_width=True)  

            # Casilla de comentarios  
            comentario = st.text_area("Por favor, cuando termines tu recorrido por la página déjanos saber tu opinión:")  
            if st.button("Enviar Comentario"):  
                st.success("¡Gracias por tu comentario!🫡")  
            
            # Opción para guardar la imagen procesada  
            st.sidebar.subheader("Guardar Imagen Procesada")  
            if procesada:  # Solo habilitar si se ha procesado alguna imagen  
                guardar = st.sidebar.selectbox("Selecciona qué imagen guardar", list(procesada.keys()))  
                if st.sidebar.button("Guardar Imagen"):  
                    if guardar:  
                        imagen_guardada = Image.fromarray(procesada[guardar])  
                        guardada = f"imagen_procesada_{guardar}.png"  
                        imagen_guardada.save(guardada)  
                        st.sidebar.write(f"Imagen guardada como {guardada}")  
            else:  
                st.sidebar.selectbox("Selecciona qué imagen guardar", ["Nada"])  # Indica que no hay procesados   

elif opcion == "No":  
    st.text("Lamentamos no poder ayudarte.😪")
