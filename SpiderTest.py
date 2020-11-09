import requests
url = 'https://www.worldometers.info/coronavirus/country/iran/'
page = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.find_all('span')) 

