import requests
import datetime
import re
from bs4 import BeautifulSoup


class EnergyScraper:
    def __init__(self):
        current_date = datetime.datetime.now().date()
        day = current_date.strftime("%d")
        month = current_date.strftime("%m")
        year = current_date.strftime("%Y")
        
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
        self.table = soup.find("div", {"class": "table-container"})

    def get_headers(self):
        self.headers = []
        temp = []
        headers = self.table.find_all(
            'th', {'class': "dv-header-right full-border vertical-center"})
        for i in headers:
            temp.append(i.find('span').text.replace('\n', ''))
        for i in range(len(temp)):
            temp[i] = temp[i].replace(' ', '')
        for item in temp:
            item = re.findall('[A-Z][a-z]*', item)
            self.headers.append(" ".join(item))
        del temp    ## free memory

    def get_data(self):
        temp = []
        self.data = []
        data = self.table.find_all('td')
        for i in data:
            target = i.find('span')
            if target == None:  # hour data and Hydro Actual Consumption don't contain span
                if i.text == '':  # Hydro Actual Consumption only, hour data: i.text, don't need them
                    target = ''
                    temp.append(target)
            else:
                temp.append(target.text)

        ## remove all Hydro Actual Consumption values
        for i in range(0, len(temp), 21):
            group = temp[i:i+21]
            del group[10]
            self.data.extend(group)

        del temp    ## free memory

    def organize_data(self):
        temp = []
        for i in self.data:
            temp.append(i)
        self.data = []
        for i in range(len(self.headers)):
            group = temp[i::len(self.headers)]      ## get every nth element, where n is the number of categories
            for j in range(len(group)):
                if group[j] == '-' or group[j] == 'N/A' or group[j] == 'n/e':       ## clean data values, make numeric
                    group[j] = 0
            self.data.append(group)
        del temp                        ## free memory

    def create_dictionary(self):
        self.get_headers()
        self.get_data()
        self.organize_data()
        self.energy_data = {self.headers[i]: self.data[i] for i in range(len(self.headers))}
        return self.energy_data
    


