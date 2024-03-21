import requests 
import bs4
import os

the_thing = requests.get("https://example.com/")
soup = bs4.BeautifulSoup(the_thing.text, 'lxml')

# print(soup.select('p')[0].getText())
# This domain is for use in illustrative examples in documents. You may use this
# domain in literature without prior coordination or asking for permission.
# ---------------------


 