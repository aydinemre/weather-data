import os
from datetime import datetime

import pandas as pd
import requests

cookies = {
    '__gads': 'ID=e50121a7c2f7ce6f-224554a3bee10063:T=1687205050:RT=1687205440:S=ALNI_Ma8kCFgqRL_oI_mFAGBTCqwdRtK5Q',
    '__gpi': 'UID=00000c51c294c2b5:T=1687205050:RT=1687205440:S=ALNI_MatrelNs0uTrFPc16YPFyimdbS04w',
}

headers = {
    'authority': 'meteostat.net',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '__gads=ID=e50121a7c2f7ce6f-224554a3bee10063:T=1687205050:RT=1687205440:S=ALNI_Ma8kCFgqRL_oI_mFAGBTCqwdRtK5Q; __gpi=UID=00000c51c294c2b5:T=1687205050:RT=1687205440:S=ALNI_MatrelNs0uTrFPc16YPFyimdbS04w',
    'pragma': 'no-cache',
    'referer': 'https://meteostat.net/en/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

cities = [
    'adana',
    'adyaman',
    'afyonkarahisar',
    'agr',
    'amasya',
    'ankara',
    'antalya',
    'artvin',
    'aydn',
    'balkesir',
    'bilecik',
    'bingol',
    'bitlis',
    'bolu',
    'burdur',
    'bursa',
    'canakkale',
    'cankr',
    'corum',
    'denizli',
    'diyarbakr',
    'edirne',
    'elazg',
    'erzincan',
    'erzurum',
    'eskisehir',
    'gaziantep',
    'giresun',
    'gumushane',
    'hakkari',
    'antakya',  # Hatay
    'isparta',
    'mersin',
    'istanbul',
    'izmir',
    'kars',
    'kastamonu',
    'kayseri',
    'krklareli',
    'krsehir',
    'izmit',  # kocaeli
    'konya',
    'kutahya',
    'malatya',
    'manisa',
    'kahramanmaras',
    'mardin',
    'mugla',
    'bulank',  # muş
    'nevsehir',
    'nigde',
    'ordu',
    'rize',
    'adapazar',  # sakarya
    'samsun',
    'siirt',
    'sinop',
    'sivas',
    'tekirdag',
    'tokat',
    'trabzon',
    'tunceli',
    'sanlurfa',
    'usak',
    'muradiye',  # van
    'yozgat',
    'zonguldak',
    'aksaray',
    'bayburt',
    'karaman',
    'krkkale',
    'batman',
    'srnak',
    'bartn',
    'ardahan',
    'igdir',
    'yalova',
    'karabuk',
    'kilis',
    'osmaniye',
    'duzce',
]
print(len(cities))

city_map = {
    'bulank': 'mus',
    'antakya': 'hatay',
    'izmit': 'kocaeli',
    'adapazar': 'sakarya',
    'muradiye': 'van',
}


def get_city_metadata(city: str):
    response = requests.get(f'https://meteostat.net/props/en/place/tr/{city}', cookies=cookies, headers=headers)
    return response.json()


def get_city_near_station(city_geo_info: dict):
    params = {
        'lat': f"{city_geo_info.get('latitude')}",
        'lon': f"{city_geo_info.get('longitude')}",
        'lang': 'en',
        'limit': '7',
    }

    response = requests.get('https://d.meteostat.net/app/nearby', params=params, headers=headers)
    return response.json().get('data', [])[0]


def get_city_weather(station_id: str) -> list:
    params = {
        'station': station_id,
        'start': '2021-01-01',
        'end': '2023-06-19',
    }

    response = requests.get('https://d.meteostat.net/app/proxy/stations/daily', params=params, headers=headers)
    return response.json()['data']


def generate_output_filename(city: str):
    city = city_map.get(city, city)
    current_date = datetime.now().strftime("%Y-%m-%d")
    os.makedirs("metostat-data", exist_ok=True)
    return f"metostat-data/{current_date}-{city}.csv"


def crawl_city_weather(city):
    output_file_name = generate_output_filename(city)
    if os.path.exists(output_file_name):
        print(f"{city} already crawled")
        return
    city_metadata = get_city_metadata(city)
    if city_metadata['status'] == 200:
        print(f"Crawling {city_metadata} Status: {city_metadata['status']}")
        near_station = get_city_near_station(city_metadata.get('place', {}).get('location', {}))
        print(f"\tNear station: {near_station.get('name')}")
        weather_data = get_city_weather(near_station.get('id'))
        city_data = pd.DataFrame(weather_data)
        city_data.to_csv(output_file_name, index=False)
    else:
        print(f"Error occured while crawling {city} Status: {city_metadata['status']}")


if __name__ == '__main__':
    for city_name in cities:
        try:
            crawl_city_weather(city_name)
        except Exception as e:
            print(f"Error occured while crawling {city_name}")
            print(e)
