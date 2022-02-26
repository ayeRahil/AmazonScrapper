import scrapy
import io
import urllib3
import urllib.request as urllib2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class SolveSpider(scrapy.Spider):
    name = 'solve'
    #allowed_domains = ['x']
    #start_urls = ['http://x/']

    def start_requests(self):
        yield scrapy.Request('https://www.amazon.com/errors/validateCaptcha')
        #,cookies={'PHPSESSID': 'xyz'}

    def parse(self, response):
        img_url = response.urljoin(response.xpath('//div[1]//div[1]/img/@src').extract_first())
        a = 'https://images-na.ssl-images-amazon.com/captcha/qamfifum/Captcha_wukyibmuwt.jpg'
        url_opener = urllib2.build_opener()
        #url_opener.addheaders.append(('Cookie', 'PHPSESSID=xyz'))
        img_bytes = url_opener.open(a).read()
        img = Image.open(io.BytesIO(img_bytes))

        captcha = pytesseract.image_to_string(img)
        print('Captcha solved:', captcha)

        headers = {'content-type': 'text/html;charset=UTF-8'}

        return scrapy.FormRequest.from_response(
            response, formdata={'captcha': captcha},
            headers = headers,
            callback=self.after_captcha)
#captchacharacters
    def after_captcha(self, response):
        print('Result:', response)
