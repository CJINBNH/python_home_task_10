import requests
from bs4 import BeautifulSoup

url = 'https://www.banki.ru/products/currency/cash/saratov/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
mass = soup.find_all(class_ = "table-flex__cell table-flex__cell--without-padding padding-left-default")
print(mass)
string = str(soup.find_all(class_ = "table-flex__cell table-flex__cell--without-padding padding-left-default"))
print(string[string.find('>')+1:string.find('</div>'):].replace(',', '.'))