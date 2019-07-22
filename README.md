# Edgar Scrapper

Edgar Scrapper is a python web scraper program that parses fund holdings pulled from EDGAR.
The program runs these following steps to retrieve and store the data:

1) Enters in a specific CIK on the <a href="https://www.sec.gov/edgar/searchedgar/companysearch.html">main page</a> and navigates to the Search Results page.

2) Finds the most recent document that has a filing that contains "13F" and navigates to the Filing Detail page (From clicking 'Documents').

3) Parses the XML table and generates a tab-delimited .csv file using that data.

## Technical Specifications

Edgar Scrapper was built using <a href="https://www.python.org/downloads/">Python 2.7.10</a> and <a href="https://docs.scrapy.org/en/latest/intro/install.html">Scrapy 1.6.0</a>.

## Getting Up and Running:

1) Assuming you've installed Python from the above link, in your console, navigate to the app's folder and run `pip install -r requirements.txt`to install all dependencies.
2) To run the program, run `scrapy runspider edgar_scrapper.py`.
3) This will generate a .csv file in the project folder based on the CIK specified in edgar_scrapper.py (Default is 0001166559).

## Author

[WilfredRuck](https://github.com/WilfredRuck) - *Public code repos*
