import requests
import csv
import os
from bs4 import BeautifulSoup

class EnergyScraper:
    def __init__(self):
        self.energy_data = {}
        self.url = 'https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&datepicker-day-offset-select-dv-date-from_input=D&dateTime.dateTime=03.04.2023+00:00|CET|DAYTIMERANGE&dateTime.endDateTime=03.04.2023+00:00|CET|DAYTIMERANGE&area.values=CTY|10YGR-HTSO-----Y!BZN|10YGR-HTSO-----Y&productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)'
        self.scrape_data()

    def fetch_soup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    
    def scrape_data(self):
        self.headers = []
        soup = self.fetch_soup()
        self.table_headers = soup.find("div",{"class":"table-container"})
        self.table_values = soup.find("table",{"id":"DataTables_Table_2"})

    def get_headers(self):
        headers = self.table_headers.find_all('th',{'class':"dv-header-right full-border vertical-center"})
        for i in headers:
            self.headers.append(i.find('span').text.replace('\n',''))
        for i in range(len(self.headers)):
            self.headers[i] = self.headers[i].replace(' ','')
        print(self.headers)
        # self.energy_data = {key: "" for key in self.headers}
        # print(self.energy_data)
    
    def get_data(self):
        temp = []
        self.data = []
        data = self.table_values.find('tbody')
        print(data)



if __name__ == '__main__':
    scraper = EnergyScraper()
    scraper.get_headers()
    scraper.get_data()
    
