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

        Result = soup.find('p', {'class': 'mt-2 text-sm leading-[22px] font-medium text-gray-primary'})
        if Result:
            Tanggal = Result.text.split(',')[0]
            Waktu = Result.text.split(',')[1]

        Result = soup.find('p', {'class': 'mt-4 text-xl lg:text-2xl font-bold text-black-primary'})
        Titik = Result.text.split(',')[0]

        Result = soup.find('span', {'class': 'text-base lg:text-lg font-bold text-black-primary'})
        Magnitudo = Result.text.split(',')

        Result = soup.find('span', {'class': 'text-base lg:text-lg font-bold text-black-primary'})
        Kedalaman = Result.text.split(',')
        # Gimana cara Inspect Elemen yang benar?

    hasil = dict()
    hasil['Tanggal'] = Tanggal #'05 Mar 2025'
    hasil['Waktu'] = Waktu #'21:35:54 WIB'
    hasil['Titik'] = Titik #'Berada di laut 30 km timur laut Lombok Utara'
    hasil['Magnitudo'] = Magnitudo #3.3
    hasil['Kedalaman'] = Kedalaman #11
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
