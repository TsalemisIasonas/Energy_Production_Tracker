import requests,csv,os
from bs4 import BeautifulSoup

class EnergyScraper:
    def __init__(self, url):
        self.url = url

    def fetch_soup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    
    def scrape_data(self):
        soup = self.fetch_soup()
        table = soup.find_all("table")#{"class":"data-view-table dataTable dv-source-table"})
        header_elements = table.find('tr',{'role':"row"})
        print(header_elements)
    




if __name__ == '__main__':
    scraper = EnergyScraper('https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&datepicker-day-offset-select-dv-date-from_input=D&dateTime.dateTime=02.04.2023+00:00|CET|DAYTIMERANGE&dateTime.endDateTime=02.04.2023+00:00|CET|DAYTIMERANGE&area.values=CTY|10YGR-HTSO-----Y!BZN|10YGR-HTSO-----Y&productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)')
    scraper.scrape_data()