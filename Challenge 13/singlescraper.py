#CHALLENGE 13 - ADAPTED FROM Y11
import requests
from bs4 import BeautifulSoup
import datetime

def filter(websitecontent):
  list = []
  for x in websitecontent:
    for i in x:
        list.append(i)
  return list

def extract(content):
  counter = 1
  list = []
  for count in range(times):
    cv = str(content[counter])#access the line with the artist name
    big = cv.index(">") + 1#find the > sing add 1 to not inculde the sign but only the song name
    small = [i for i, n in enumerate(cv) if n == '<'][1]#a beautiful piece of code that finds the second instance of < since index would only give the first < at 0
    list.append((cv[big:small]))#splice them up to inculde the artis only
    counter += 3#go onto the next artist line ,skipping the <div> lines and such
  return list

if __name__ == '__main__':
  URL = ('https://www.officialcharts.com/charts/singles-chart/')
  page = requests.get(URL) #access website
  
  times = 10
  soup = BeautifulSoup(page.content, 'html.parser')
  
  longtitle = soup.findAll("div", {"class": "title"}, limit=times) 
  seperate = filter(longtitle)
  songs = extract(seperate)
  
  longartist = soup.findAll("div", {"class": "artist"}, limit=times) 
  aseperate = filter(longartist)
  artists = extract(aseperate)
  
  date = datetime.date.today()
  print("Top 10 Official Singles")
  print(f"As of {date}:")
  for x in range(times):
      print(f"{x + 1}. {songs[x]} - {artists[x]}")