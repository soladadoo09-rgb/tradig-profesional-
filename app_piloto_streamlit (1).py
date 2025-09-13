# app_piloto.py
import streamlit as st
import random

# ====== Configuración de la página ======
st.set_page_config(page_title="Pro Trading App Piloto", layout="wide")

# ====== Menú lateral ======
st.sidebar.title("📊 Menú")
opcion = st.sidebar.radio("Selecciona opción:", ["Inicio", "Análisis", "Pausa", "Fin"])

if opcion == "Inicio":
    st.title("📈 Bienvenido a Pro Trading App Piloto")
    st.write("Esta es una versión simple de la app de trading. No usa librerías externas.")

elif opcion == "Análisis":
    st.subheader("📊 Datos simulados del mercado")
    precios_simulados = [100, 102, 101, 105, 107]
    st.write("Precios simulados:", precios_simulados)
    
    st.subheader("📰 Noticias simuladas")
    noticias = [
        "Mercado estable",
        "Inversores optimistas",
        "Noticias neutrales",
        "Alerta de volatilidad"
    ]
    noticia = random.choice(noticias)
    st.write("Noticia:", noticia)
    
    if "optimista" in noticia.lower():
        st.success("Sentimiento positivo")
    elif "alerta" in noticia.lower():
        st.error("Sentimiento negativo")
    else:
        st.info("Sentimiento neutral")

elif opcion == "Pausa":
    st.warning("⏸️ Análisis en pausa. Presiona 'Análisis' para continuar.")

elif opcion == "Fin":
    st.error("🛑 Análisis terminado. Reinicia la app para iniciar de nuevo.")