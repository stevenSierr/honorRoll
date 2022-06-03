from bs4 import BeautifulSoup
import requests
import pandas as pd

# extract data from "https://osuokc.edu/honorroll/VP-FA18"
# Fall 2o18 Honor Roll
response = requests.get("https://osuokc.edu/honorroll/VP-FA18")
content = response.content
soup = BeautifulSoup(content, 'lxml')
names = soup.find_all('p') 

# set empty array
x = []

# p denotes paragraph tags
for p in names:
    # x is the array where you push (append) all the <p> tags
    x.append(p.text)

# use pandas and xlsxwriter to import array into Excel
data = pd.DataFrame({ 'Data': x })
writer = pd.ExcelWriter('honor_Roll.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name='Fall 2018')
writer.save()
