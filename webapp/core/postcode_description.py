from bs4 import BeautifulSoup
import requests

from webapp.core.postcodes import data


class PostcodeBuilder:

    def connect(self, postcode: str):
        website = requests.get(f'https://www.postcodearea.co.uk/postaltowns/london/{postcode}/')
        soup = BeautifulSoup(website.content, 'html.parser')

        return soup

    def get_all_postcodes(self, postcode: str):
        soup = self.connect(postcode)
        postcode_list = []
        postcodes = soup.find_all(class_='btn btn-primary btn-block btn-sm')
        for post_code in postcodes:
            postcode_list.append(post_code.text)

        return postcode_list


    def get_stats(self, postcode: str):
        soup = self.connect(postcode)
        results = []
        stats = soup.find_all(class_='giant')
        for stat in stats:
            integers = []
            for in_stat in stat.text:
                if in_stat.isnumeric():
                    integers.append(in_stat)

            num = int(''.join(map(str, integers)))
            results.append(num)
        population, households, unemployment, household_income = results

        return {
            "population": population,
            "households": households,
            "unemployment": unemployment,
            "household_income": household_income
        }


    def get_sentence(self, postcode: str):
        soup = self.connect(postcode)
        info = soup.find_all('strong')
        info = info[0].text
        return info
