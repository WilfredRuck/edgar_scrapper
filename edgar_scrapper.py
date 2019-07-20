import scrapy
from bs4 import BeautifulSoup

class BlogSpider(scrapy.Spider):
  name = 'blogspider'
  cik = '0001166559'
  base_url = 'https://www.sec.gov'
  xml_page_url = ''
  # start_url = 'https://www.sec.gov/Archives/edgar/data/1166559/000110465919029714/0001104659-19-029714-index.htm'
  start_url = 'https://www.sec.gov/edgar/searchedgar/companysearch.html'
  start_urls = [start_url]

  def parse(self, response):
    return scrapy.FormRequest.from_response(
        response,
        formnumber=4,
        formdata={'CIK': '0001166559'},
        callback=self.parse_filings
    )

  # def parse_filings(self, response):
  #   filings = []
  #   for filing in response.css('div#contentDiv'):
  #     filings.append(filing.css('div.noCompanyMatch::text').get())
  #     if file is not None and "13F" in file:
  #       filings.append(filing.css('td::text').get())
  #   for next_page in response.css('a.next-posts-link'):
  #       yield response.follow(next_page, self.parse_filings)
  #   print(filings)
  #   print(response.url)

  def parse_filings(self, response):
    for filing in response.css('tr'):
      file = filing.css('td::text').get()
      if file is not None and "13F" in file:
        self.xml_page_url = filing.css('a#documentsbutton::attr(href)').extract()[0]
        break
    yield scrapy.Request(self.base_url + self.xml_page_url, callback=self.parse_xml)
    # for next_page in response.css('a.next-posts-link'):
    #     yield response.follow(next_page, self.parse)

  def parse_xml(self, response):
    f = open("data.txt","w+")
    products = response.css('tr')
    # ignore the table header row
    for product in products[1:]:
       item = dict()
       item['seq'] = product.xpath('td[1]//text()').extract_first()
       item['description'] = product.xpath('td[2]//text()').extract_first()
       item['document'] = product.xpath('td[3]//text()').extract_first()
       item['type'] = product.xpath('td[3]//text()').extract_first()
       item['size'] = product.xpath('td[3]//text()').extract_first()
       for k, v in item.items():
        if v is None:
          item[k] = ""
       val_string = ','.join(item.values())
       f.write(val_string + '\n')