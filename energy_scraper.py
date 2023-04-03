import requests
import csv
import os
from bs4 import BeautifulSoup

class EnergyScraper:
    def __init__(self):
        self.energy_data = {}
        self.url = 'https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show'
        self.scrape_data()

    def fetch_soup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    
    def scrape_data(self):
        self.headers = []
        soup = self.fetch_soup()
        self.table = soup.find("div",{"class":"table-container"})

    def get_headers(self):
        headers = self.table.find_all('th',{'class':"dv-header-right full-border vertical-center"})
        for i in headers:
            self.headers.append(i.find('span').text.replace('\n',''))
        for i in range(len(self.headers)):
            self.headers[i] = self.headers[i].replace(' ','')
        # self.energy_data = {key: "" for key in self.headers}
        # print(self.energy_data)
    
    def get_data(self):
        temp = []
        self.data = []
        data = self.table.find('tbody')
        rows = data.find_all('tr')
        print(len(rows))
        for row in rows:
            containers = row.find_all('td')
            temp.append(containers)
            # for container in containers:
            #     value = container.find('span')
            #     temp.append(value)
            for i in temp:
                print(i)



if __name__ == '__main__':
    scraper = EnergyScraper()
    # scraper.get_headers()
    scraper.get_data()
    
