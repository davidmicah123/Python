from bs4 import BeautifulSoup
import requests

url = "https://www.scrapethissite.com/pages/frames/"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")

link = soup.find_all('a')

# print(soup)
print(link)