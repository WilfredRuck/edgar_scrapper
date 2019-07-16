import scrapy

class BlogSpider(scrapy.Spider):
  name = 'blogspider'
  start_urls = ['https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001166559&owner=exclude&action=getcompany&Find=Search']

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