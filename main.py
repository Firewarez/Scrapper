####################################################################################
##                                                                                ##
##   Scrapper for events in Sympla website                                        ##
##   By: Arthur Barcelos as a computer science student                            ##
##                                                                                ##
##   Date: Dec 2025                                                               ##
##   License: GNU GENERAL PUBLIC LICENSE                                          ##
##   Description: This script main scrapper Rock eventes from sympla in Brazil    ##
##   You can change the link variable and main rules to scrapp other events       ##
##                                                                                ##
##                                                                                ##
##                                                                                ##
####################################################################################
import requests
from bs4 import BeautifulSoup

link = 'https://www.sympla.com.br/eventos/joao-pessoa-pb/show-musica-festa'
response = requests.get(link)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')


# Find main element card which is base for other elements
cards = soup.find_all('a', class_='sympla-card')

# Find Title of the event
title = soup.find_all('h3', class_='pn67h1c')

# Find P element for event location
location = soup.find_all('p', class_='pn67h1e')

# Find Div element for event date and time
dates = soup.find_all('div', class_='qtfy415 qtfy413 qtfy416')

for card in cards:
    card_title = card.find('h3', class_='pn67h1c').get_text()
    card_location = card.find('p', class_='pn67h1e').get_text()
    card_date = card.find('div', class_='qtfy415 qtfy413 qtfy416').get_text()
    print(f'Title: {card_title}\nLocation: {card_location}\nDate: {card_date}\n')

