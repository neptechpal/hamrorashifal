from bs4 import BeautifulSoup
import requests

from urllib import request

class Hamrorashifal:
    
    def scraperashifal(self):
        base = "https://www.hamropatro.com/"
        url = "https://www.hamropatro.com/rashifal/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        rashifals = soup.find_all('div',{"class":"item"})
        

        rashifallist = []

       

        for rashifal in rashifals:
          items = {
                'title': rashifal.find('h3').text.strip(),
                'description':  rashifal.find('div',{"class":"desc"}).text.strip(),
                'image': base+rashifal.find('img')['src']
                   }
          rashifallist.append(items)
          print(rashifallist)
          
        return rashifallist


myverydata = Hamrorashifal()
myverydata.scraperashifal()

mylist = [
    "Mesh",
    "Brish",
    "Mithun",
    "Karkat",
    "Singha",
    "Kanya",
    "Tula",
    "Brischik",
    "Dhanu",
    "Makar",
    "Kumbha",
    "Meen"]

class WeeklyRashifal:
 def weeklyrashifal(self,mylist,time):
    rashifallisty = []
    for items in mylist:
        url = "https://www.hamropatro.com/rashifal/"+time+"/"+items+"/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_head = soup.find_all('h2',{"class":"maintitle"})
        description = soup.find_all('div',{"class":"desc"})

        items = {

        }

        

        # print(description)
        for titles in title_head:
            mytitle = titles.find('span').text
            items['title'] = mytitle

        for descriptions in description:
            desc = descriptions.find('p').text.strip()
            items['description'] = desc
        
        
        rashifallisty.append(items)
        
    # print(rashifallist)
    return rashifallisty

