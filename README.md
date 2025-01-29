# AliExpress Web Scraper
## Description
This Python script scrapes product details from AliExpress using Selenium, Helium, and lxml. It extracts product titles, prices, ratings, manufacturers, and links across multiple pages and stores the data in a CSV file. The script automates browsing, scrolling, and data extraction to collect valuable marketplace insights.

## Features
**Automated Web Scraping:** Uses Selenium and Helium to navigate and scroll through AliExpress pages.

**Data Extraction:** Captures product details including:
```bash
-Title
-Price
-Rating
-Manufacturer
-Product Link
-Page Number
```
**CSV Export:** Saves extracted data to project.csv for further analysis.\

**Pagination Support:** Scrapes multiple pages (default: first 10 pages).

## Technology Stack

Python 3.x

Selenium (for browser automation)

Helium (simplified Selenium interactions)

lxml (for efficient HTML parsing)

csv (for structured data storage)
## Code Overview
**Main Steps:**

**-Initialize WebDriver**

  Opens AliExpress and dynamically loads pages.

**-Loop Through Pages**

  Iterates through first 10 pages (range(1,10)).

**-Extract Data**

  Uses XPath selectors to grab product details.
  
**-Store Data**

Writes extracted information into a CSV file.
