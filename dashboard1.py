import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data heatmap
heatmap_data1 = pd.read_csv("shunyiPM2.5.csv")  # Ganti dengan nama file CSV
heatmap_data2 = pd.read_csv("shunyiPM10.csv")  # Ganti dengan nama file CSV
heatmap_data3 = pd.read_csv("tiantanPM2.5.csv")  # Ganti dengan nama file CSV
heatmap_data4 = pd.read_csv("tiantanPM10.csv")  # Ganti dengan nama file CSV

# Load data plotline
plotline1 = pd.read_csv("shunyiPM2.5stats.csv")  # Ganti dengan nama file CSV
plotline2 = pd.read_csv("shunyiPM10stats.csv")  # Ganti dengan nama file CSV
plotline3 = pd.read_csv("tiantanPM2.5stats.csv")  # Ganti dengan nama file CSV
plotline4 = pd.read_csv("tiantanPM10stats.csv")  # Ganti dengan nama file CSV

st.sidebar.title("Kualitas Udara dikota Shunyi dan Tiantan")
filter_choice = st.sidebar.radio("silahkan pilih topik", ("Tren", "Perbedaan"))

if filter_choice == "Tren":
    st.title("Tren Kualitas Udara")
    st.write("data menunjukkan kualitas udara pada kota shunyi dan tiantan pada tahun 2014, kadar polutan (PM2.5, PM10) pada bulan kedua adalah yang tertinggi, dan yang terendah pada bulan ke-enam")
    st.write("Pilih Lokasi dan Polutan:")

    # Filter untuk memilih lokasi dan polutan
    location = st.selectbox("Pilih Lokasi", ("Shunyi", "Tiantan"))
    polutan = st.selectbox("Pilih Polutan", ("PM2.5", "PM10"))

    st.write("perlu diperhatikan bahwa indeksnya dimulai dari 0 sebagai januari sampai 11 sebagai desember")

    if location == "Shunyi" and polutan == "PM2.5":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(heatmap_data1, ax=ax, annot=True, fmt=".1f", cmap="viridis")
        st.pyplot(fig)
    elif location == "Shunyi" and polutan == "PM10":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(heatmap_data2, ax=ax, annot=True, fmt=".1f", cmap="viridis")
        st.pyplot(fig)
    elif location == "Tiantan" and polutan == "PM2.5":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(heatmap_data3, ax=ax, annot=True, fmt=".1f", cmap="viridis")
        st.pyplot(fig)
    elif location == "Tiantan" and polutan == "PM10":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(heatmap_data4, ax=ax, annot=True, fmt=".1f", cmap="viridis")
        st.pyplot(fig)

elif filter_choice == "Perbedaan":
    st.title("Perbedaan Kualitas Udara")
    st.write("Pilih Lokasi dan Polutan:")

    # Filter untuk memilih lokasi dan polutan
    location = st.selectbox("Pilih Lokasi", ("Shunyi", "Tiantan"))
    polutan = st.selectbox("Pilih Polutan", ("PM2.5", "PM10"))

    st.write("perlu diperhatikan bahwa indeksnya dimulai dari 0 sebagai januari sampai 11 sebagai desember")

    if location == "Shunyi" and polutan == "PM2.5":
        fig, ax = plt.subplots()
        plotline1['mean'].plot(ax=ax, kind='line')
        plt.xlabel('Bulan')  # Gunakan plt.xlabel() di sini
        plt.ylabel('PM2.5')
        st.pyplot(fig)
        st.title('Rata-rata PM2.5 per Bulan dikota Shunyi tahun 2014')
    elif location == "Shunyi" and polutan == "PM10":
        fig, ax = plt.subplots()
        plotline2['mean'].plot(ax=ax, kind='line')
        plt.xlabel('Bulan')  # Gunakan plt.xlabel() di sini
        plt.ylabel('PM10')
        st.pyplot(fig)
        st.title('Rata-rata PM10 per Bulan dikota Shunyi tahun 2014')
    elif location == "Tiantan" and polutan == "PM2.5":
        fig, ax = plt.subplots()
        plotline3['mean'].plot(ax=ax, kind='line')
        plt.xlabel('Bulan')  # Gunakan plt.xlabel() di sini
        plt.ylabel('PM2.5')
        st.pyplot(fig)
        st.title('Rata-rata PM2.5 per Bulan dikota Tiantan tahun 2014')
    elif location == "Tiantan" and polutan == "PM10":
        fig, ax = plt.subplots()
        plotline4['mean'].plot(ax=ax, kind='line')
        plt.xlabel('Bulan')  # Gunakan plt.xlabel() di sini
        plt.ylabel('PM10')
        st.pyplot(fig)
        st.title('Rata-rata PM10 per Bulan dikota Tiantan tahun 2014')