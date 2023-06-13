import streamlit as st
import numpy as np

def svd_calculator(matrix):
    # Melakukan SVD pada matriks
    U, s, Vt = np.linalg.svd(matrix)
    return U, s, Vt

# Judul aplikasi
st.title("Calkulator Singular Value Decomposition (SVD) ")

# Input data
st.header("Masukkan Matriks")
rows = st.number_input("Jumlah Baris", min_value=1, step=1, value=2)
cols = st.number_input("Jumlah Kolom", min_value=1, step=1, value=2)
matrix = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = st.number_input(f"Elemen [{i+1}, {j+1}]")

# Tombol untuk menghitung SVD
if st.button("Hitung"):
    # Memanggil fungsi svd_calculator untuk menghitung SVD
    U, s, Vt = svd_calculator(matrix)
    st.subheader("Hasil")
    st.write("Matriks U:")
    st.write(U)
    st.write("Nilai Singular:")
    st.write(s)
    st.write("Matriks V Transpos:")
    st.write(Vt)
