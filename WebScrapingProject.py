# web_scraping using BeautifulSoup4 and requests
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the number of pages to parse",type=int)
parser.add_argument("--dbname",help="Enter the number of db",type=str)
args = parser.parse_args()

oyo_url = "https://www.oyoroom.com/hotels-in-bangalore/?page="


