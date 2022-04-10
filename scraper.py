from bs4 import BeautifulSoup
import requests

from urllib import request

class Hamrorashifal:
    def scraperashifal(self):
        url = "https://www.hamropatro.com/rashifal/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        rashifals = soup.find_all('div',{"class":"item"})

        rashifallist = []

       

        for rashifal in rashifals:
          items = {
                'title': rashifal.find('h3').text.strip(),
                'description': rashifal.find('div',{"class":"desc"}).text.strip(),
                'image':rashifal.find('img')['src']
                   }
          rashifallist.append(items)
        #   print(rashifallist)
          
        return rashifallist
            
        # items = soup.find_all('a')
     

       
        # print("Rashifals are",rashifals)
Hamrorashifal.scraperashifal(Hamrorashifal,)