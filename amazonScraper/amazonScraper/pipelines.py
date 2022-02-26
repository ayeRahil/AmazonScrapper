# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter
#from sqlalchemy.orm import sessionmaker

#from .models import Items, create_items_table, db_connect
import mysql.connector

class AmazonscraperPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = mysql.connector.connect(
            host= 'localhost',
            user = os.environ['user'],
            passwd = os.environ['passwd'],
            database = 'prod_details'
        )
        self.curr = self.conn.cursor()



    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS details_tb""")
        self.curr.execute("""create table details_tb(
                        Title text,
                        Image_url text,
                        Price text,
                        Details text)""")



    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into details_tb values (%s, %s, %s, %s)""",(
            item['Title'],
            item['Image_url'],
            item['Price'],
            item['Details'],
        ))

        self.conn.commit()