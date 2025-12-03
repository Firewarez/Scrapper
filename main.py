import requests
from bs4 import BeautifulSoup

link = 'https://www.sympla.com.br/eventos/joao-pessoa-pb/show-musica-festa'
response = requests.get(link)

soup = BeautifulSoup(response.text, 'html.parser')

# Find Title of the event
soup.find_all('h3', class_='pn67h1c')

# Find P element for event location
soup.find_all('p', class_='pn67h1e')

# Find Div element for event date and time
soup.find_all('div', class_='qtfy415 qtfy413 qtfy416')

items = soup.find_all('div', class_='qtfy415 qtfy413 qtfy416')
for item in items:
    print(item.get_text())

