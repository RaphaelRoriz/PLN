import unicodedata
from bs4 import BeautifulSoup

def strip_html_tags(text):
	soup = BeautifulSoup(text,"html.parser")
	stripped_text = soup.get_text()
	return stripped_text

#print(strip_html_tags('<html><h2>Some important text</h2></html>'))