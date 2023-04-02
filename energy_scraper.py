import requests
import csv
import os
from bs4 import BeautifulSoup

class EnergyScraper:
    def __init__(self):
        self.url = 'https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show'

    def fetch_soup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    
    def scrape_data(self):
        self.headers = []
        soup = self.fetch_soup()
        table = soup.find("div",{"class":"table-container"})
        headers = table.find_all('th',{'class':"dv-header-right full-border vertical-center"})
        for i in headers:
            self.headers.append(i.find('span').text.replace('\n',''))
        for i in range(len(self.headers)):
            self.headers[i] = self.headers[i].replace(' ','')
            
        return self.headers


# if __name__ == '__main__':
#     scraper = EnergyScraper()
#     scraper.scrape_data()
