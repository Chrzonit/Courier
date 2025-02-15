import feedparser
import pprint
import streamlit as st
from xhtml2pdf import pisa
from dotenv import load_dotenv
import os


feed_urls = [{'feed': 'Dwarkesh', 'url': 'https://www.dwarkeshpatel.com/feed'}]

parsed_feed = feedparser.parse(feed_urls[0]['url'])
print(type(parsed_feed))
print(parsed_feed.keys())
print(parsed_feed['feed'])
print(parsed_feed['entries'][0].keys())
print(len(parsed_feed['entries']))
print(parsed_feed['namespaces'])

pprint.pprint(parsed_feed['entries'][0].content[0].value)

with open('output.pdf', 'wb') as f:
    pisa.CreatePDF(parsed_feed['entries'][0].content[0].value, f)
    
    
