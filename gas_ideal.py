import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Kalkulator Gas Ideal", page_icon="🧪", layout="wide")

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
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
    st.markdown(r"""
    **Persamaan Gas Ideal:**  
    \[
    PV = nRT
    \]
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
    st.subheader("(SELAMAT DATANG DI PV-nRTin Aja)")

    st.markdown("""
### Penjelasan mengenai gas ideal 
Gas ideal adalah sekumpulan partikel gas yang tidak berinteraksi satu sama lain. Partikel-partikel gas ideal tersebar dengan jarak yang besar di antara mereka dan bergerak secara acak.

#### Hukum-Hukum Gas Ideal:
- **Hukum Boyle**: Pada suhu konstan, volume gas berbanding terbalik dengan tekanannya.
- **Hukum Charles**: Pada tekanan konstan, volume gas berbanding lurus dengan suhunya.
- **Hukum Gay-Lussac**: Pada volume konstan, tekanan gas berbanding lurus dengan suhunya.

#### Sifat-Sifat Gas Ideal:
1. Partikel gas selalu bergerak secara acak
2. Tidak memiliki gaya tarik-menarik antarmolekul
3. Ukuran partikel sangat kecil dibanding volume ruang
4. Distribusi partikel merata
5. Tumbukan antar partikel bersifat lenting sempurna
""")

    # Tambahkan data dummy
    data = pd.DataFrame({
        "Volume (L)": [1, 2, 3, 4, 5],
        "Tekanan (atm)": [5, 2.5, 1.67, 1.25, 1.0]
    })

    # Buat grafik
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
    
    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam L", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821  # konstanta gas

    hitung = st.button("Hitung")

    if hitung:
        hasil = None
        if P == 0 and V != 0 and n != 0 and T != 0:
            P = (n * R * T) / V
            hasil = f"Tekanan (P) = {P:.2f} atm"
        elif V == 0 and P != 0 and n != 0 and T != 0:
            V = (n * R * T) / P
            hasil = f"Volume (V) = {V:.2f} L"
        elif n == 0 and P != 0 and V != 0 and T != 0:
            n = (P * V) / (R * T)
            hasil = f"Jumlah mol (n) = {n:.2f} mol"
        elif T == 0 and P != 0 and V != 0 and n != 0:
            T = (P * V) / (n * R)
            hasil = f"Suhu (T) = {T:.2f} K"
        else:
            hasil = "Tolong kosongkan tepat satu variabel (isi dengan 0) untuk dihitung."

        st.success(hasil)

    st.caption("Menggunakan R = 0.0821 L·atm/mol·K")
