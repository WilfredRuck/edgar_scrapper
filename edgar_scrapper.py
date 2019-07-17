import scrapy

class BlogSpider(scrapy.Spider):
  name = 'blogspider'
  cik = '0001166559'
  start_url = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=' + cik + '&owner=exclude&action=getcompany&Find=Search'
  start_urls = [start_url]

  # def parse(self, response):
  #   # text = str(text).encode('utf-8')
  #   return scrapy.FormRequest.from_response(
  #       str(response.css('form#fast-search')).encode('utf-8'),
  #       formdata={'cik': '0001166559'},
  #       callback=self.parse_filings
  #   )

  # def parse_filings(self, response):
  #   # filings = []
  #   # for filing in response.css('div#contentDiv'):
  #   #   filings.append(filing.css('div.noCompanyMatch::text').get())
  #     # if file is not None and "13F" in file:
  #     #   filings.append(filing.css('td::text').get())
  #   # for next_page in response.css('a.next-posts-link'):
  #   #     yield response.follow(next_page, self.parse)
  #   # print(filings)
  #   print(response.url)

  def parse(self, response):
    filings = []
    for filing in response.css('tr'):
      file = filing.css('td::text').get()
      if file is not None and "13F" in file:
        filings.append(filing.css('td::text').get())
    # for next_page in response.css('a.next-posts-link'):
    #     yield response.follow(next_page, self.parse)
    print(filings)
    print(len(filings))