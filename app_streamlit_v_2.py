# app_streamlit.py
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from textblob import TextBlob
import random

# ====== Configuración de la página ======
st.set_page_config(page_title="Pro Trading App V2", layout="wide")

# ====== Menú lateral ======
st.sidebar.title("📊 Menú")
opcion = st.sidebar.radio("Selecciona opción:", ["Inicio", "Análisis", "Pausa", "Fin"])

if opcion == "Inicio":
    st.title("📈 Bienvenido a Pro Trading App V2")
    st.write("Visualiza gráficos, indicadores y noticias del mercado en tiempo real.")

elif opcion == "Análisis":
    ticker = st.text_input("Ticker (Ej: AAPL, BTC-USD):", "AAPL")
    if ticker:
        df = yf.download(ticker, period="1mo", interval="1h")
        df.reset_index(inplace=True)
        
        # ====== Gráfico de velas con colores dinámicos ======
        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=df['Datetime'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            increasing_line_color='green',
            decreasing_line_color='red',
            name="Velas"
        ))
        fig.update_layout(height=600, title=f"Gráfico de {ticker}")
        st.plotly_chart(fig, use_container_width=True)
        
        # ====== Indicadores técnicos básicos ======
        df['SMA_5'] = df['Close'].rolling(window=5).mean()
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        st.line_chart(df[['SMA_5', 'SMA_20']])
        
        # ====== Noticias simuladas y análisis de sentimiento ======
        noticias = [
            "Empresa reporta ganancias mejores de lo esperado",
            "Mercado en incertidumbre por cambios políticos",
            "Nueva regulación afecta al sector tecnológico",
            "Inversores optimistas por crecimiento económico"
        ]
        noticia = random.choice(noticias)
        st.subheader("Noticia del mercado:")
        st.write(noticia)
        sentimiento = TextBlob(noticia).sentiment.polarity
        if sentimiento > 0:
            st.success("Sentimiento positivo")
        elif sentimiento < 0:
            st.error("Sentimiento negativo")
        else:
            st.info("Sentimiento neutral")

elif opcion == "Pausa":
    st.warning("⏸️ Análisis en pausa. Presiona 'Análisis' para continuar.")

elif opcion == "Fin":
    st.error("🛑 Análisis terminado. Reinicia la app para iniciar de nuevo.")
