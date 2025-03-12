import requests
from bs4 import BeautifulSoup



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

    global Tanggal
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        Result1 = soup.find('p', {'class': 'mt-2 text-sm leading-[22px] font-medium text-gray-primary'})
        if Result1:
            Tanggal = Result1.text.split(',')[0]
            Waktu = Result1.text.split(',')[1]
        Result2 = soup.find('p', {'class': 'mt-4 text-xl lg:text-2xl font-bold text-black-primary'})
        if Result2:
            Titik = Result2.text.split(',')[0]


    hasil = dict()
    hasil['Tanggal'] = Tanggal #'05 Mar 2025'
    hasil['Waktu'] = Waktu #'21:35:54 WIB'
    hasil['Titik'] = Titik #'Berada di laut 30 km timur laut Lombok Utara'
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
