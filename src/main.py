import feedparser
import pprint
import streamlit as st
from xhtml2pdf import pisa
from dotenv import load_dotenv
import os
from .remarkable.api import reMarkable


feed_urls = [{'feed': 'Dwarkesh', 'url': 'https://www.dwarkeshpatel.com/feed'}]

parsed_feed = feedparser.parse(feed_urls[0]['url'])

pprint.pprint(parsed_feed['entries'][0].content[0].value)

with open('output.pdf', 'wb') as f:
    pisa.CreatePDF(parsed_feed['entries'][0].content[0].value, f)
    
    
remarkable = reMarkable()

remarkable.get_device_token()
remarkable.refresh_user_token()

with open('.env', 'w') as file:
    file.write(f"DEVICE_TOKEN = {remarkable.device_token}\nUSER_TOKEN = {remarkable.user_token}") 