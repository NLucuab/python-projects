import requests
from bs4 import BeautifulSoup

"""
This is a website webscraper that utilizes BeautifulSoup. 
This was made to be used to gather the updated COVID19 stats of Washington State, USA.
"""

URL = "https://www.worldometers.info/coronavirus/usa/washington/"
page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.content, "lxml")
# print(soup.prettify)

results = soup.find(id="usa_table_countries_today")
# print(results)

content = results.find_all("td") 
# print(content)

# Used this for loop to print out only the text information within the code block for the table.
# I was able to check the code using command + f for the specific state information that I need. 
# for entries in content:
#     print(entries.text.strip())

counties = [] # good
total_cases = []
new_cases = []
total_deaths = [] # good
new_deaths = []


i = 0
for entry in content:
    if i % 8 == 0:
        counties.append(entry.text.strip())
    elif i % 8 == 1:
        total_cases.append(entry.text.strip())
    elif i % 8 == 2:
        new_cases.append(entry.text.strip())
    elif i % 8 == 3:
        total_deaths.append(entry.text.strip())
    elif i % 8 == 4:
        new_deaths.append(entry.text.strip())
    i += 1

# print(counties)
# print(total_cases)
# print(new_cases)
# print(total_deaths)
# print(new_deaths)


