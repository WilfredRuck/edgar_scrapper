import scrapy

class EdgarSpider(scrapy.Spider):
  name = 'edgarspider'
  cik = '0001166559'
  base_url = 'https://www.sec.gov'
  xml_page_url = ''
  start_url = 'https://www.sec.gov/edgar/searchedgar/companysearch.html'
  start_urls = [start_url]

  def parse(self, response):
    return scrapy.FormRequest.from_response(
        response,
        formnumber=4,
        formdata={'CIK': '0001166559'},
        callback=self.parse_filings
    )

  def parse_filings(self, response):
    for filing in response.css('tr'):
      file = filing.css('td::text').get()
      if file is not None and "13F" in file:
        self.xml_page_url = filing.css('a#documentsbutton::attr(href)').extract()[0]
        break
    yield scrapy.Request(self.base_url + self.xml_page_url, callback=self.parse_xml)

  def parse_xml(self, response):
    f = open("data.txt","w+")
    products = response.css('tr')
    for i, product in enumerate(products):
       item = dict()
       if i == 0:
        item['seq'] = product.xpath('th[1]//text()').extract_first()
        item['description'] = product.xpath('th[2]//text()').extract_first()
        item['document'] = product.xpath('th[3]//text()').extract_first()
        item['type'] = product.xpath('th[4]//text()').extract_first()
        item['size'] = product.xpath('th[5]//text()').extract_first()
       else:
        item['seq'] = product.xpath('td[1]//text()').extract_first()
        item['description'] = product.xpath('td[2]//text()').extract_first()
        item['document'] = product.xpath('td[3]//text()').extract_first()
        item['type'] = product.xpath('td[4]//text()').extract_first()
        item['size'] = product.xpath('td[5]//text()').extract_first()
        for k, v in item.items():
          if v is None:
            item[k] = ""
       val_string = ','.join(item.values())
       f.write(val_string + '\n')