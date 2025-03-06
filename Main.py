"""
Aplikasi Deteksi Gempa
Modularisasi dengan fuction
"""
import Deteksi_Gempa

if __name__ == '__main__' :
    print('Laporan Gempa Terkini')
    result = Deteksi_Gempa.ekstraksi_data()
    Deteksi_Gempa.tampilkan_data(result)

