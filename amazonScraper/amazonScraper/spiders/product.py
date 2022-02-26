import scrapy
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from ..items import AmazonscraperItem
from pandas import DataFrame as df

sheet_url = "https://docs.google.com/spreadsheets/d/1BZSPhk1LDrx8ytywMHWVpCqbm8URTxTJrIRkD7PnGTM/edit#gid=0"
url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
df = pd.read_csv(url_1)
#df = df.head(100)
df1 = df[['Asin', 'country']]

class ProductSpider(scrapy.Spider):
    name = 'product'
    # allowed_domains = ['x']
    # start_urls = ['http://x/']

    def start_requests(self):
        self.count = 0
        for i, row in df1.iterrows():
            asin = row['Asin']
            country = row['country']
            site = "https://www.amazon.{}/dp/{}".format(country, asin)
            self.count += 1
            yield scrapy.Request(site)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        item = AmazonscraperItem()
        if response.status == 200:

            title = soup.find("span",attrs={"id": 'productTitle'})
            title_value = title.string
            title_string = title_value.strip().replace(',', '')
            item['Title'] = title_string

            try:
                img = soup.find("img", attrs={"id": 'imgBlkFront'})["src"]
            except TypeError:
                img = soup.find("img", attrs={"id": 'landingImage'})["src"]
            except :
                img = "NA"
            finally:
                item["Image_url"] = img


            try:
                prices = soup.find_all("a", attrs={"class":"a-button-text"})
                x = None
                for p in prices:
                    x = p.find("span", attrs={'class': 'a-color-base'})
                price = x.text.replace("\n","").replace("  ","")
            except AttributeError:
                price = "NA"
            finally:
                item["Price"] = price



            try:
                detail = soup.find("div", attrs={"id": 'featurebullets_feature_div'})
                detail = detail.text.strip()
            except AttributeError:
                #detail = detailBullets_feature_div
                desc = soup.find("div", attrs={"id": 'detailBullets_feature_div'})
                desc = desc.text.strip()
                detail = desc.replace("\n","").replace("  ","")

            except:
                detail = "NA"
            finally:
                item["Details"] = detail
            '''item = {
                'title': response.css('#productTitle ::text').get(),
                'image_url': response.css('#imgBlkFront::attr(src)').extract_first(),
                'price': response.css('span.a-color-base > span ::text').get(),
                'detail': response.css('#detailBulletsWrapper_feature_div ::text').get(),
            }'''
        else:
            if response.status == 404:
               print(response.url," not available")

        if not bool(item):
            pass
        else:
            yield item

    def close(self, reason):
        start_time = self.crawler.stats.get_value('start_time')
        #finish_time = self.crawler.stats.get_value('finish_time')
        if self.count % 100 == 0:
            finish_time = datetime.datetime.now()
            print("Time taken for 100 url ", finish_time - start_time)

        '''printcounter = 0

        # Whatever a while loop is in Python
        while (self.count<=1000):
            if (printcounter == 100):
                print("Time taken for 100 urls ", finish_time - start_time)
                printcounter = 0
            printcounter += 1'''