import pickle
import streamlit as st

# Load Model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb')) 

# Judul Web 
st.title('Prediksi Penyakit Diabetes')

Pregnancies = st.text_input('Masukkan Nilai Pregnancies : ')

Glucose = st.text_input('Masukkan Nilai Glucose : ')

BloodPressure = st.text_input('Masukkan Nilai Blood Pressure : ')

SkinThickness = st.text_input('Masukkan Nilai Skin Thickness : ')

Insulin = st.text_input('Masukkan Nilai Insulin : ')

BMI = st.text_input('Masukkan Nilai BMI : ')

DiabetesPedigreeFunction = st.text_input('Masukkan Nilai Diabetes Pedigree Function : ')

Age = st.text_input('Masukkan Nilai Age : ')

# Code Untuk Prediksi
diabetes_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Tes Prediksi Diabetes') :
    diabetes_prediksi = diabetes_model.predict([[
    Pregnancies,
    Glucose,
    BloodPressure,
    SkinThickness,
    Insulin,
    BMI,
    DiabetesPedigreeFunction,
    Age
]]);

    if(diabetes_prediksi[0] == 1) : 
        diabetes_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'
    st.success(diabetes_diagnosis)