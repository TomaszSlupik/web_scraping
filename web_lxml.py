# załadowanie bibliotek:
import requests
from lxml import html


url = 'https://m.bankier.pl/notowania/nbp/USD'

res = requests.get(url)


if res.status_code == 200:
    print(res)
    
# Liczba wszytskich divów: 
tree = html.fromstring(res.content)
div = tree.xpath('//div')
print(f"Liczba wsyztskich div: {len(div)}")


# Wydrukowanie konkretnego h2:
dolar = tree.xpath('//h2[@class="secondHeader"]/text()')
for txt in dolar:
    print(txt)

# Wydrukowanie spana:
dolarNumber = tree.xpath('//span[@class="profileLast"]/text()')

for num in dolarNumber:
    print(num)



