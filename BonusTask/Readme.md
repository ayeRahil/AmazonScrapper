# Captcha Solver
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
___
This Captcha Solver is made using using Scrapy and several Python libraries.
___
___
#### This task is done partially. I got the part to resolve the captchas but wasn't able to submit the form.
___
Run the spider by following the commands given below:
```python
cd BonusTask/amazonScraper
scrapy crawl solve
```

___
Approach
* Visits the URL and extracts the src of img of the Captcha.
* Then the img is converted into Binary data using Pillow library
* The Binary data is passed through the Tesseract lib to convert it to String
* It returns the solved captcha.
___
