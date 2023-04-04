import requests,datetime,re
import csv
import os
from bs4 import BeautifulSoup

class EnergyScraper:
    def __init__(self):
        current_date = datetime.datetime.now().date()
        day = current_date.strftime("%d")
        month = current_date.strftime("%m")
        year = current_date.strftime("%Y")
        self.energy_data = {}
        part1 = f'https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show?name=&defaultValue=true&viewType=TABLE&areaType=BZN&atch=false&datepicker-day-offset-select-dv-date-from_input=D&dateTime.dateTime={day}.{month}.{year}+00:00'
        part2 = f'|CET|DAYTIMERANGE&dateTime.endDateTime={day}.{month}.{year}+00:00|CET|DAYTIMERANGE&area.values=CTY|10YGR-HTSO-----Y!BZN|10YGR-HTSO-----Y&'
        part3 = 'productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)'
        self.url = part1+part2+part3
 
                    

        self.scrape_data()

    def fetch_soup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    
    def scrape_data(self):
        soup = self.fetch_soup()
        self.table = soup.find("div",{"class":"table-container"})
        

    def get_headers(self):
        self.headers = []
        temp = []
        headers = self.table.find_all('th',{'class':"dv-header-right full-border vertical-center"})
        for i in headers:
            temp.append(i.find('span').text.replace('\n',''))
        for i in range(len(temp)):
            temp[i] = temp[i].replace(' ','')
        for item in temp:
            item = re.findall('[A-Z][a-z]*', item)
            self.headers.append(" ".join(item))
        temp = []
        print(self.headers)
        # self.energy_data = {key: "" for key in self.headers}
        # print(self.energy_data)
    
    def get_data(self):
        temp = []
        self.data = []
        # data = self.table.find_all('div',{'class':'dataTables_wrapper'},{'role':'grid'})
        data = self.table.find_all('span')
        data = data[len(self.headers)+2:]
        for i in data:
            temp.append(i.text)
        for i in temp:
            print(i)



if __name__ == '__main__':
    scraper = EnergyScraper()
    scraper.get_headers()
    scraper.get_data()
    
