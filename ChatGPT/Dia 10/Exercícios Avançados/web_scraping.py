import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Vamos obter o título da página
title = soup.title.string
print(title)

# Vamos obter todos os links da página
links = soup.find_all("a")
for link in links:
    print(link["href"])
