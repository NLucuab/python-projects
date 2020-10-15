import requests
from bs4 import BeautifulSoup

"""
This is a website webscraper that utilizes BeautifulSoup. 
This was made to be used to gather the updated COVID19 stats of Washington State, USA.
I utilized Wayscript.com in order to send myself daily text message updates using the data collected by this code.
I have also changed this code (on Wayscript.com) in order to collect information from 2 counties in New York & 1 in Pennsylvania (in order to send updates to friends).
"""

URL = "https://www.worldometers.info/coronavirus/usa/washington/"
page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.content, "lxml")
# lxml is a BeautifulSoup parser. It can be used to parse XML and HTML. 

# print(soup.prettify)

results = soup.find(id="usa_table_countries_today")
# print(results)

content = results.find_all("td") 
# print(content)

"""
Used this for loop to print out only the text information within the code block for the table.
I was able to check the code using command + f for the specific state information that I need.
"""
# for entries in content:
#     print(entries.text.strip())

outputs = {}

i = 0
while i < len(content):
    if content[i].text.strip() != 'King':
        i+=1
        continue
    outputs['total cases'] = content[i+1].text.strip()
    outputs['new cases'] = content[i+2].text.strip()
    outputs['total deaths'] = content[i+3].text.strip()
    outputs['new deaths'] = content[i+4].text.strip()
    break
print(outputs)