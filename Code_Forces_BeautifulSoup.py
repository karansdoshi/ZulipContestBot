from bs4 import BeautifulSoup
import requests


url = "http://codeforces.com/contests/"

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')
dict={}

values=soup.find_all('table')
values=values[0]
for row in values.find_all('tr'):
    if(len(row.find_all('td'))>0):
        dict[row.find_all('td')[0].text.strip()]=[row.find_all('td')[2].text.strip(),row.find_all('td')[3].text.strip()]

print(dict)
