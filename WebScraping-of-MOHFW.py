from bs4 import BeautifulSoup
import pandas as pd
url="C:\\Users\\Asikul\\Documents\\mohfw\\MOHFW.html"

soup = BeautifulSoup(open(url,mode='r',encoding='utf-8'),"html.parser")
table = soup.find('table',class_="statetable table table-striped")

records = []
for row in table.find_all("tr"):
    for col in table.find_all("td"):
        state = col.text
        records.append(state)

COVID_19 = pd.DataFrame(records)
COVID_19.to_csv("covid19_py2.csv")
print("Data succesfully scrapped.")
