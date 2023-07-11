from bs4 import BeautifulSoup as BS
import requests

url = 'http://www.jumia.com.ng/sporting-goods/'
response = requests.get(url)
contents = BS(response.text, 'html.parser')
section= contents.find("section", class_="card -oh")
container = contents.find('div', class_='row _no-g -tac -pvxs -phs _6c-shs')
items = container.find_all('div', class_='ar _3-4')

for item in items:
    image = item.find('img', class_='-rad4')
    print()
    print(image['data-src'])
    print()