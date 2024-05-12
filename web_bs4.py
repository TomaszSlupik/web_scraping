import requests
from bs4 import BeautifulSoup

my_url = 'https://www.onet.pl'

res = requests.get(my_url)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.title.string
    print(f"Tytuł strony oneta: ${title}")

print('---')

if res.status_code == 200:
    imgs = soup.find('a', class_="Common_BigCardLink__1rnMf")
    text_img = imgs.find('h3').text
    print(text_img)