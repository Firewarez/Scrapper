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


title = soup.find_all('h3', class_='pn67h1c')
for item in title:  
    print("Title: " + item.get_text())
    
location = soup.find_all('p', class_='pn67h1e')
for item in location:
    print("Location: " + item.get_text())

dates = soup.find_all('div', class_='qtfy415 qtfy413 qtfy416')
for item in dates:
    print("Date: " + item.get_text())

