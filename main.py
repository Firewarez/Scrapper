# -*- coding: utf-8 -*-
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
#import sys
#import io

# Fix Windows console encoding for UTF-8
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

link = 'https://www.sympla.com.br/eventos/joao-pessoa-pb/show-musica-festa'
response = requests.get(link)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')


# Find main element card which is base for other elements
cards = soup.find_all('a', class_='sympla-card')

## JUST TEST SLOOP
# Find Title of the event
#title = soup.find_all('h3', class_='pn67h1c')

# Find P element for event location
#location = soup.find_all('p', class_='pn67h1e')

# Find Div element for event date and time
#dates = soup.find_all('div', class_='qtfy415 qtfy413 qtfy416')

for card in cards:
    card_title_element = card.find('h3', class_='pn67h1c')
    title = card_title_element.get_text() if card_title_element else "Title not found"
    
    card_location_element = card.find('p', class_='pn67h1e')
    location = card_location_element.get_text() if card_location_element else "Location not found"
    
    card_date_element = card.find('div', class_='qtfy415 qtfy413 qtfy416')
    date = card_date_element.get_text() if card_date_element else "Date not found"
    
    print(f'Title: {title}\nLocation: {location}\nDate: {date}\n')

