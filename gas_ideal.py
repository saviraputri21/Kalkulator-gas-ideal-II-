
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Kalkulator Gas Ideal", page_icon="🧪", layout="wide")

# Sidebar untuk navigasi
menu = st.sidebar.selectbox(
    "Pilih Halaman",
    ["🏠 Home", "📊 Dashboard", "🧮 Kalkulator"]
)

# --------------------------
# 🏠 HALAMAN HOME
# --------------------------
if menu == "🏠 Home":
    st.title("🧪 Aplikasi Kalkulator Gas Ideal")
    st.header("Penjelasan Singkat")
    st.markdown("""
    **Persamaan Gas Ideal:**  
    \n\\( PV = nRT \\)  
    
    - **P**: Tekanan (atm)  
    - **V**: Volume (L)  
    - **n**: Jumlah mol  
    - **R**: Konstanta gas (0.0821 L·atm/mol·K)  
    - **T**: Suhu (K)
    
    Aplikasi ini membantu Anda menghitung salah satu variabel jika variabel lainnya diketahui.
    """)
    st.info("Pilih menu di sebelah kiri untuk mencoba kalkulator atau melihat dashboard grafik.")

# --------------------------
# 📊 HALAMAN DASHBOARD
# --------------------------
elif menu == "📊 Dashboard":
    st.title("📊 Dashboard Gas Ideal")
    
    st.subheader("(SELAMAT DATANG DI PV-nRTin Aja )")
    
     st.markdown("""
 ### Penjelasan mengenai gas ideal 
     Gas ideal adalah sekumpulan partikel gas yang tidak berinteraksi satu sama lain. Partikel-partikel gas ideal tersebar dengan jarak yang besar di antara mereka dan bergerak secara acak.

Hukum - Hukum Gas Ideal 
• Hukum Boyle: Pada suhu konstan, volume suatu gas berbanding terbalik dengan tekanannya.
• Hukum Charles: Pada tekanan konstan, volume suatu gas berbanding lurus dengan suhunya.
• Hukum Gay-Lussac: Pada volume konstan, tekanan suatu gas berbanding lurus dengan suhunya.

*Sifat-Sifat Gas Ideal*
Berlaku Hukum newton tentang gerak
1. Partikel Gas Selalu bergerak secara acak atau sembarang
2. Tidak mempunyai gaya tarik menarik/intyeraksi antarmolekul
3. Ukuran molekul gas dapat diabaikan terhadap ukuran ruangan tempat gas berada
4. Partikel gas terdistribusi merata dalam ruangan
5. Tumbukan antar partikel bersifat lenting sempurna

     
    # Plot
    fig, ax = plt.subplots()
    ax.plot(data["Volume (L)"], data["Tekanan (atm)"], marker='o', color='teal')
    ax.set_xlabel("Volume (L)")
    ax.set_ylabel("Tekanan (atm)")
    ax.set_title("P vs V (n dan T konstan)")
    st.pyplot(fig)
    
    st.info("Grafik ini menunjukkan hukum Boyle: tekanan dan volume berbanding terbalik jika jumlah mol (n) dan suhu (T) tetap.")

# --------------------------
# 🧮 HALAMAN KALKULATOR
# --------------------------
elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Gas Ideal")

    st.markdown("Isi variabel yang diketahui. Kosongkan (isi 0) variabel yang ingin dihitung.")

    # Input
    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam L", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821

    # Tombol hitung
    hitung = st.button("Hitung")

    if hitung:
        hasil = None
        # Hitung P jika P == 0
        if P == 0 and V !=0 and n !=0 and T !=0:
            P = (n * R * T) / V
            hasil = f"Tekanan (P) = {P:.2f} atm"
        # Hitung V jika V == 0
        elif V == 0 and P !=0 and n !=0 and T !=0:
            V = (n * R * T) / P
            hasil = f"Volume (V) = {V:.2f} L"
        # Hitung n jika n == 0
        elif n == 0 and P !=0 and V !=0 and T !=0:
            n = (P * V) / (R * T)
            hasil = f"Jumlah mol (n) = {n:.2f} mol"
        # Hitung T jika T == 0
        elif T == 0 and P !=0 and V !=0 and n !=0:
            T = (P * V) / (n * R)
            hasil = f"Suhu (T) = {T:.2f} K"
        else:
            hasil = "Isi semua variabel kecuali satu (kosongkan variabel yang ingin dihitung dengan 0)."
        
        st.success(hasil)

    st.caption("Menggunakan R = 0.0821 L·atm/mol·K")

st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪")

st.title("🧪 Kalkulator Hukum Gas Ideal")
st.write("Gunakan persamaan PV = nRT untuk menghitung salah satu variabel.")

st.latex("PV = nRT")
st.markdown("Dengan R = 0.0821 L·atm/mol·K")

# Input variabel
P = st.number_input("Tekanan (P) dalam atm (kosongkan jika ingin dihitung)", min_value=0.0, format="%.4f")
V = st.number_input("Volume (V) dalam liter (kosongkan jika ingin dihitung)", min_value=0.0, format="%.4f")
n = st.number_input("Jumlah mol (n) (kosongkan jika ingin dihitung)", min_value=0.0, format="%.4f")
T = st.number_input("Suhu (T) dalam Kelvin (kosongkan jika ingin dihitung)", min_value=0.0, format="%.2f")

R = 0.0821  # L·atm/mol·K

# Deteksi input kosong
inputs = {'P': P, 'V': V, 'n': n, 'T': T}
empty_vars = [var for var, value in inputs.items() if value == 0.0]

if st.button("Hitung"):
    if len(empty_vars) != 1:
        st.error("Tolong kosongkan tepat satu variabel untuk dihitung.")
    else:
        if P == 0.0:
            P = (n * R * T) / V
            st.success(f"Tekanan (P) = {P:.4f} atm")
        elif V == 0.0:
            V = (n * R * T) / P
            st.success(f"Volume (V) = {V:.4f} liter")
        elif n == 0.0:
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol (n) = {n:.4f} mol")
        elif T == 0.0:
            T = (P * V) / (n * R)
            st.success(f"Suhu (T) = {T:.2f} K")
