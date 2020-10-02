import requests
from bs4 import BeautifulSoup
"""
A simple web scraper project, focusing on obtaining the href links within the a tags 
in all of the h2 tags on the 'Briefings & Statements' webpage on the whitehouse.gov website.
"""

# Let's obtain the links from the following website: 
# https://www.whitehouse.gov/briefings-statements/

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find("a")
    urls.append(a_tag.attrs['href'])
print(urls)