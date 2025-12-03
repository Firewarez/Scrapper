# Sympla Event Scrapper

A web scraper for extracting event information from Sympla, Brazil's popular event ticketing platform.

## Description

This Python script scrapes event data from Sympla's website, including event titles, locations, and dates. The scraper is currently configured to fetch rock music events and shows from João Pessoa, PB, but can be easily modified to scrape events from other locations or categories.

## Features

- Extracts event titles, locations, and dates
- UTF-8 encoding support for Portuguese characters
- Clean, readable output format
- Easy to customize for different event categories and locations

## Requirements

- Python 3.x
- requests
- beautifulsoup4

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install requests beautifulsoup4
pip install requests
```

## Usage

Simply run the script:
```bash
python main.py
```

To scrape events from different locations or categories, modify the `link` variable in `main.py`:
```python
link = 'https://www.sympla.com.br/eventos/[city-state]/[category]'
```

## Output Example

```
Title: BAILE DAS CACHORRAS com KAYA CONKY
Location: Clube Metrópole - Recife, PE
Date: Sexta, 19 de Dez às 22:00
```

## License

GNU General Public License

## Author

Arthur Barcelos - Computer Science Student

---
*December 2025*
