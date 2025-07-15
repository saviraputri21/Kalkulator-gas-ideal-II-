import streamlit as st

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
