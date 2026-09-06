import streamlit as st
import joblib
import numpy as np

model = joblib.load("grid_model.pkl")
scaler = joblib.load("grid_scaler.pkl")

st.title("⚡ Smart Grid Stability Predictor")
st.markdown("Elektr tarmog'i sozlamalari asosida barqarorlikni bashorat qilish")

st.subheader("Reaksiya vaqtlari (tau)")
col1, col2, col3, col4 = st.columns(4)
with col1:
    tau1 = st.number_input("tau1", 0.5, 10.0, 5.0)
with col2:
    tau2 = st.number_input("tau2", 0.5, 10.0, 5.0)
with col3:
    tau3 = st.number_input("tau3", 0.5, 10.0, 5.0)
with col4:
    tau4 = st.number_input("tau4", 0.5, 10.0, 5.0)

st.subheader("Quvvat (p)")
col1, col2, col3, col4 = st.columns(4)
with col1:
    p1 = st.number_input("p1", 0.0, 5.0, 3.0)
with col2:
    p2 = st.number_input("p2", -2.0, 0.0, -1.0)
with col3:
    p3 = st.number_input("p3", -2.0, 0.0, -1.0)
with col4:
    p4 = st.number_input("p4", -2.0, 0.0, -1.0)

st.subheader("Narx sezgirligi (g)")
col1, col2, col3, col4 = st.columns(4)
with col1:
    g1 = st.number_input("g1", 0.05, 1.0, 0.5)
with col2:
    g2 = st.number_input("g2", 0.05, 1.0, 0.5)
with col3:
    g3 = st.number_input("g3", 0.05, 1.0, 0.5)
with col4:
    g4 = st.number_input("g4", 0.05, 1.0, 0.5)

if st.button("Predict"):
    data = np.array([[tau1, tau2, tau3, tau4, p1, p2, p3, p4, g1, g2, g3, g4]])
    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)[0]
    proba = model.predict_proba(data_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Unstable (Nobarqaror) — ehtimollik: {proba:.2%}")
    else:
        st.success(f"✅ Stable (Barqaror) — ehtimollik: {(1-proba):.2%}")