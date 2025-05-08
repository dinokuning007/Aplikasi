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

    try:
        content = requests.get('https://stamet-yogya.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {'class': 'list-gempa'})

        Tanggal = Waktu = None

        if result:
            text: str = result.get_text(separator='\n').strip()
            lines = text.splitlines()

            if len(lines) >= 2:
                Tanggal = lines[0].strip()
                Waktu = lines[1].strip()

        Magnitudes = soup.find_all('p')

        Magnitude = None
        for p in Magnitudes:
            if 'Magnitude' in p.text:
                Magnitude = p.text.strip().split(':')[-1].strip()

        Pusats = soup.find_all('p')

        Pusat = None
        for p in Pusats:
            if 'Pusat' in p.text:
                 Pusat = p.text.strip().split(':')[-1].strip()

        Kedalamans = soup.find_all('p')

        Kedalaman = None
        for p in Kedalamans:
            if "Kedalaman" in p.text:
                Kedalaman = p.text.strip().split(':')[-1].strip()

        divs = soup.find_all('div')

        LS = None
        BT = None
        for div in divs:
            if 'LS' in div.text and 'BT' in div.text:
                print (div.text)

    hasil = dict()
    hasil['Tanggal'] = Tanggal or 'Tidak ada'
    hasil['Waktu'] = Waktu or 'Tidak ada'
    hasil['Titik'] = Pusat
    hasil['Magnitudo'] = Magnitude
    hasil['Kedalaman'] = Kedalaman
    hasil['LS'] = LS
    hasil['BT'] = BT

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan data dari BMKG')
    print('Tanggal', result['Tanggal'])
    print(f"Waktu {result['Waktu']}")
    print('Titik', result['Titik'])
    print(f"Magnitudo {result['Magnitudo']} SR")
    print(f"Kedalaman {result['Kedalaman']}")
    print(f"Lintang Selatan {result['LS']}")
    print(f"Bujur Timur {result['BT']}")


if __name__ == '__main__':
    print('Breaking News')
