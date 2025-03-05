"""
Aplikasi Deteksi Gempa
Modularisasi dengan fuction
"""
from Deteksi_Gempa import ekstraksi_data, tampilkan_data

if __name__ == '__main__' :
    print('Laporan Gempa Terkini')
    result = ekstraksi_data()
    tampilkan_data(result)

