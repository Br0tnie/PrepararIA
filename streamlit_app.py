import streamlit as st

st.title("🎈 My new app")
st.write(
    "SAS [docs.streamlit.io](https://docs.streamlit.io/)."

)
st.subheader("Selecciona tu tipo de alimentación")
tipo_alimentacion = st.selectbox("Tipo de alimentación", ["Omnívoro", "Vegetariano", "Vegano", "Celíaco", "Diabético"])
