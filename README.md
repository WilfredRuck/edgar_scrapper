# Edgar Scrapper

Edgar Scrapper is a program that parses fund holdings pulled from EDGAR, given a ticker or CIK, and writes a .tsv file from them.

## Technical Specifications

Edgar Scrapper was built using <a href="https://www.python.org/downloads/">Python 2.7.10</a> and <a href="https://docs.scrapy.org/en/latest/intro/install.html">Scrapy 1.6.0</a>.

## Getting Up and Running:
<ol>
<li> Assuming you've installed Python from the above link, in your console, navigate to the app's folder and run `pip install -r requirements.txt`to install all dependencies.</li>
<li>To run the program, run `scrapy runspider edgar_scrapper.py`.</li>
<li>This will generate a .csv file in the project folder based on the CIK specified in edgar_scrapper.py (Default is 0001166559).</li>
</ol>

## Author

[WilfredRuck](https://github.com/WilfredRuck) - *Public code repos*
