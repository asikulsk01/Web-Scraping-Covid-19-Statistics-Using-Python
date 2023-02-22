import requests

from bs4 import BeautifulSoup

import pandas as pd

url = "https://www.technoindiauniversity.ac.in/"

r = requests.get(url)
print(r)

htmlCon = r.content
print(htmlCon)

soup = BeautifulSoup(htmlCon, 'html.parser')
print(soup)
data = soup.find_all('div',class_ ='single-content')
print(data)

records =[]

for lists in data:

    schoolnm = lists.find('a').text

    dessc = lists.find('p').text

    records.append((schoolnm, dessc))

df = pd.DataFrame(records, columns = ['school', 'description'])
df.to_csv('Assignment1_py.csv')
print('School data is Sussessfully Extracted')
