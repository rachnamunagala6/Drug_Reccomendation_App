import scrapy
from webmd_scraper.items import WebmdScraperItem

class WebMDSpider(scrapy.Spider):
    custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    name = "webmd"
    start_urls = ['http://www.webmd.com/drugs/2/index']

    def parse(self, response):
        items = []

        # Extract drug information and yield items
        drug_names = response.css('a.common-drug-name::text').getall()
        print(f"Found {len(drug_names)} drug names:", drug_names)

        for drug_name in drug_names:
            item = WebmdScraperItem()
            item["drug_name"] = drug_name.strip()  
            items.append(item)

        return items

