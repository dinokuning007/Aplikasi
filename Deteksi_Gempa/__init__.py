def ekstraksi_data():
    """
    Tanggal: 05 Mar 2025
    Waktu: 21:35:54 WIB
    Titik: berada di laut 30 km timur laut Lombok Utara
    Magnitudo: 3,3
    Kedalaman: 11 Km
    Long: 8,18
    Lat: -116,38 BT
    :return:
    """
    hasil = dict()
    hasil['Tanggal'] = '05 Mar 2025'
    hasil['Waktu'] = '21:35:54 WIB'
    hasil['Titik'] = 'Berada di laut 30 km timur laut Lombok Utara'
    hasil['Magnitudo'] = 3.3
    hasil['Kedalaman'] = 11
    hasil['LS'] = 8.18
    hasil['BT'] = -116.38

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan data dari BMKG')
    print('Tanggal', result['Tanggal'])
    print(f"Waktu {result['Waktu']}")
    print('Titik', result['Titik'])
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Kedalaman {result['Kedalaman']} Km")
    print(f"Lintang Selatan {result['LS']}")
    print(f"Bujur Timur {result['BT']}")


if __name__ == '__main__':
    print('Breaking News')

