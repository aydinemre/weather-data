
# Weather Data Crawler

This repository contains the Weather Data Crawler, a tool that pulls weather data from different online sources, processes it, and stores it in a structured format for future use.

## Table of Contents
1. Introduction
2. Getting Started
3. Usage
4. Contributing
5. License

## Introduction

The Weather Data Crawler is designed to obtain accurate and up-to-date weather data. This crawler is particularly useful for projects requiring data like temperature, humidity, wind speed, precipitation, etc., from multiple locations worldwide. It scrapes this information from public weather data sources and stores it in a clean, structured format.

Please note that this crawler is respectful of terms of service of the data sources and includes time delay between requests to avoid overloading the server. Make sure to familiarize yourself with the terms of use of the data sources before using this crawler.

## Getting Started
### Prerequisites

- Python 3.x
- Libraries: BeautifulSoup, requests, pandas

To install the required libraries, use the following command:

```bash
pip install beautifulsoup4 requests pandas selenium
```

### Installation
1. Clone the repo
```bash
git clone https://github.com/your_username_/WeatherDataCrawler.git
```
2. Install Python packages
```bash
pip install -r requirements.txt
```
3. Usage
To run the crawler:

```bash
python wunderground.py 
python metostat.py
```

The program will output a CSV file containing the weather data.

### Contributing
Contributions are what make the open source community an incredible place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

### License
Distributed under the MIT License. See LICENSE for more information.

<b>Note</b>: This is a basic README template for your project. You might need to update the URLs, project specifics, etc. according to your needs. Moreover, please ensure that any data crawling performed is in compliance with the terms of service of the websites from which you are extracting data.