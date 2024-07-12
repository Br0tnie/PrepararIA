import streamlit as st


st.page_link("your_app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)

st.title("PrepararIA: Caso de uso 1.")
st.write(
    "SAS [docs.streamlit.io](https://docs.streamlit.io/)."

)
# Sección para seleccionar tipo de alimentación
st.subheader("Selecciona tu tipo de alimentación")
tipo_alimentacion = st.selectbox("Tipo de alimentación", ["Omnívoro", "Vegetariano", "Vegano", "Celíaco", "Diabético"])

# Sección para seleccionar tipo de preparación
st.subheader("Selecciona el tipo de preparación")
tipo_preparacion = st.selectbox("Tipo de preparación", ["Desayuno", "Cena", "Postre", "Almuerzo"])
