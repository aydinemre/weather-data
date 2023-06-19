import os
from datetime import datetime
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

cities = [
    'https://www.wunderground.com/weather/tr/istanbul',
    'https://www.wunderground.com/weather/tr/ankara',
    'https://www.wunderground.com/weather/tr/i%CC%87zmir',

    'https://www.wunderground.com/weather/tr/adana',
    'https://www.wunderground.com/weather/tr/ad%C4%B1yaman',
    'https://www.wunderground.com/weather/tr/afyonkarahisar',
    'https://www.wunderground.com/weather/tr/a%C4%9Fr%C4%B1',
    'https://www.wunderground.com/weather/tr/aksaray',
    'https://www.wunderground.com/weather/tr/amasya',
    'https://www.wunderground.com/weather/tr/antalya',
    'https://www.wunderground.com/weather/tr/ardahan',
    'https://www.wunderground.com/weather/tr/artvin',
    'https://www.wunderground.com/weather/tr/ayd%C4%B1n',
    'https://www.wunderground.com/weather/tr/bal%C4%B1kesir',
    'https://www.wunderground.com/weather/tr/bart%C4%B1n',
    'https://www.wunderground.com/weather/tr/batman',
    'https://www.wunderground.com/weather/tr/bayburt',
    'https://www.wunderground.com/weather/tr/bilecik',
    'https://www.wunderground.com/weather/tr/bing%C3%B6l',
    'https://www.wunderground.com/weather/tr/bitlis',
    'https://www.wunderground.com/weather/tr/bolu',
    'https://www.wunderground.com/weather/tr/burdur',
    'https://www.wunderground.com/weather/tr/bursa',
    'https://www.wunderground.com/weather/tr/%C3%A7anakkale',
    'https://www.wunderground.com/weather/tr/hand%C4%B1r%C4%B1',
    'https://www.wunderground.com/weather/tr/%C3%A7orum',
    'https://www.wunderground.com/weather/tr/denizli',
    'https://www.wunderground.com/weather/tr/diyarbak%C4%B1r',
    'https://www.wunderground.com/weather/tr/d%C3%BCzce',
    'https://www.wunderground.com/weather/tr/edirne',
    'https://www.wunderground.com/weather/tr/elaz%C4%B1%C4%9F',
    'https://www.wunderground.com/weather/tr/erzincan',
    'https://www.wunderground.com/weather/tr/erzurum',
    'https://www.wunderground.com/weather/tr/eski%C5%9Fehir',
    'https://www.wunderground.com/weather/tr/gaziantep',
    'https://www.wunderground.com/weather/tr/giresun',
    'https://www.wunderground.com/weather/tr/g%C3%BCm%C3%BC%C5%9Fhane',
    'https://www.wunderground.com/weather/tr/hakk%C3%A2ri',
    'https://www.wunderground.com/weather/tr/hatay-province',
    'https://www.wunderground.com/weather/tr/i%C4%9Fd%C4%B1r',
    'https://www.wunderground.com/weather/tr/isparta',
    'https://www.wunderground.com/weather/tr/marash',
    'https://www.wunderground.com/weather/tr/karab%C3%BCk',
    'https://www.wunderground.com/weather/tr/karaman',
    'https://www.wunderground.com/weather/tr/kars',
    'https://www.wunderground.com/weather/tr/kastamonu',
    'https://www.wunderground.com/weather/tr/kayseri',
    'https://www.wunderground.com/weather/tr/k%C4%B1r%C4%B1kkale',
    'https://www.wunderground.com/weather/tr/k%C4%B1rklareli',
    'https://www.wunderground.com/weather/tr/k%C4%B1r%C5%9Fehir',
    'https://www.wunderground.com/weather/tr/kilis',
    'https://www.wunderground.com/weather/tr/kocaeli-province',
    'https://www.wunderground.com/weather/LTAN',
    'https://www.wunderground.com/weather/tr/konya',
    'https://www.wunderground.com/weather/tr/k%C3%BCtahya',
    'https://www.wunderground.com/weather/tr/malatya',
    'https://www.wunderground.com/weather/tr/manisa',
    'https://www.wunderground.com/weather/tr/mardin',
    'https://www.wunderground.com/weather/tr/mersin',
    'https://www.wunderground.com/weather/tr/mu%C4%9Fla',
    'https://www.wunderground.com/weather/tr/mu%C5%9F',
    'https://www.wunderground.com/weather/tr/nev%C5%9Fehir',
    'https://www.wunderground.com/weather/tr/ni%C4%9Fde',
    'https://www.wunderground.com/weather/tr/ordu',
    'https://www.wunderground.com/weather/tr/osmaniye',
    'https://www.wunderground.com/weather/tr/rize',
    'https://www.wunderground.com/weather/tr/sakarya-province',
    'https://www.wunderground.com/weather/tr/samsun',
    'https://www.wunderground.com/weather/tr/siirt',
    'https://www.wunderground.com/weather/tr/sinop',
    'https://www.wunderground.com/weather/tr/sivas',
    'https://www.wunderground.com/weather/tr/%C5%9Fanl%C4%B1urfa',
    'https://www.wunderground.com/weather/tr/%C5%9F%C4%B1rnak',
    'https://www.wunderground.com/weather/tr/tekirda%C4%9F',
    'https://www.wunderground.com/weather/tr/tokat',
    'https://www.wunderground.com/weather/tr/trabzon',
    'https://www.wunderground.com/weather/tr/tunceli',
    'https://www.wunderground.com/weather/tr/u%C5%9Fak',
    'https://www.wunderground.com/weather/tr/van',
    'https://www.wunderground.com/weather/tr/yalova',
    'https://www.wunderground.com/weather/tr/yozgat',
    'https://www.wunderground.com/weather/tr/zonguldak'
]

TABLE_XPATH = '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]'


def get_history_url(driver, city_url):
    driver.get(city_url)
    # Wait until page elements are loaded
    print(f"Trying to pass accept cookies button for {city_url}")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="truste-consent-button"]'))
    ).click()

    # Wait until history button is loaded
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="inner-content"]/div[2]/lib-city-header/div[2]/lib-subnav/div/div[3]/ul/li[5]/a/span'))
    ).click()
    # Implicitly Wait until page elements are loaded
    driver.implicitly_wait(30)
    history_url = driver.current_url.replace('daily', 'monthly')
    if 'monthly' not in history_url:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="inner-content"]/div[2]/lib-city-header/div[2]/lib-subnav/div/div[3]/ul/li[5]/a/span'))
        ).click()
        history_url = driver.current_url.replace('daily', 'monthly')
    if 'Error 404' in driver.page_source:
        return city_url.replace('weather', 'history/monthly')
    return history_url


def crawl_city(history_url, driver,
               start_date=datetime(year=2021, month=1, day=1),
               end_date=datetime.now()):
    city_datas = []
    date_range = pd.date_range(start_date, end_date, freq='MS').tolist()
    for date in date_range:
        current_url = history_url + f"/date/{date.year}-{date.month}"
        print(current_url)
        driver.get(current_url)
        sleep(10)
        # Wait until page elements are loaded
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, TABLE_XPATH)))
        # Implicitly Wait until page elements are loaded
        driver.implicitly_wait(30)
        # Read table as dataframe
        monthly_table = driver.find_element(By.XPATH, TABLE_XPATH)
        tables = pd.read_html(monthly_table.get_attribute('outerHTML'), flavor='html5lib')
        city_data = {
            'dates': [datetime(year=date.year, month=date.month, day=int(day)) for day in tables[1].loc[1:, 0]],
            'Max Temperature (°F)': tables[2][0].loc[1:].tolist(),
            'Avg Temperature (°F)': tables[2][1].loc[1:].tolist(),
            'Min Temperature (°F)': tables[2][2].loc[1:].tolist(),
            'Max Dew Point (°F)': tables[3][0].loc[1:].tolist(),
            'Avg Dew Point (°F)': tables[3][1].loc[1:].tolist(),
            'Min Dew Point (°F)': tables[3][2].loc[1:].tolist(),
            'Max Humidity (%)': tables[4][0].loc[1:].tolist(),
            'Avg Humidity (%)': tables[4][1].loc[1:].tolist(),
            'Min Humidity (%)': tables[4][2].loc[1:].tolist(),
            'Max Wind Speed (mph)': tables[5][0].loc[1:].tolist(),
            'Avg Wind Speed (mph)': tables[5][1].loc[1:].tolist(),
            'Min Wind Speed (mph)': tables[5][2].loc[1:].tolist(),
            'Max Pressure (in)': tables[6][0].loc[1:].tolist(),
            'Avg Pressure (in)': tables[6][1].loc[1:].tolist(),
            'Min Pressure (in)': tables[6][2].loc[1:].tolist(),
            'Precipitation (in)': tables[7][0].loc[1:].tolist(),
        }
        city_datas.append(pd.DataFrame(city_data))

    # Convert to dataframe
    return pd.concat(city_datas)


def generate_output_filename(city_url: str):
    current_date = datetime.now().strftime("%Y-%m-%d")
    city_name = city_url.split('/')[-1]
    return f"wunderground-data/{current_date}-{city_name}.csv", city_name


def crawl_city_weather(city_url: str) -> None:
    # Generate filename

    output_file, city_name = generate_output_filename(city_url)
    print(f"Starting to crawl {city_name} Output file: {output_file}")
    # Check file exists
    if os.path.exists(output_file):
        print(f"{city_name}.csv already exists")
        return

    # Create chrome driver
    driver = webdriver.Chrome()
    # Get city history url from city url
    city_history_url = get_history_url(driver, city_url)
    # Set crawler start and end date
    start_date = datetime(year=2022, month=1, day=1)
    end_date = datetime.now()
    # Crawl city wunderground-data
    city_data = crawl_city(city_history_url, driver, start_date=start_date, end_date=end_date)
    # Save city wunderground-data
    city_data.to_csv(output_file, index=False)


if __name__ == '__main__':
    for city_url in cities:
        try:
            crawl_city_weather(city_url)
        except Exception as e:
            print(f"Error occured while crawling {city_url}")
            print(e)
