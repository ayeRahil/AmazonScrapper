# Amazon Scraper
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
___
This scraper was made using using Scrapy and BeautifulSoup.
___
Run the spider by following the commands given below:
```python
cd amazonScraper
scrapy crawl product
```

___
Approach
* The data given in the Google Sheet is used using Pandas library. Only the necessary columns are accessed which are "Asin" and "Country".
* Using formating in Python and iterating over the rows to access each url.
* Each data is extracted using BeautifulSoup.
* If any URL is not found than print "{URL} not available".
* Available data is yeilded in result.json file.
* Connected the scraper to the MYSQL Database using pipelines.py file.
___
## Bonus Task
* Added Google Collab badge.
* Connected to MYSQL database.