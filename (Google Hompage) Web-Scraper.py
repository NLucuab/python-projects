import requests
from bs4 import BeautifulSoup

"""
Introdcution to web scraping (in Python) project as found in the Beautiful Soup Tutorial on freeCodeCamp.org
"""

result = requests.get("https://www.google.com/")

# To make sure that the website is accessible, check for a 200 OK response.
# print(result.status_code)

# The HTTP header of the website can also be checked to verify that we have accessed the correct page.
# print(result.headers)

# The page content can pe stored in a variable for easier access
src = result.content

# The BeautifulSoup module can be used to parse and process the source.
soup = BeautifulSoup(src, 'lxml')

# After BeautifulSoup has processed the page source, we can access specific information from it.
links = soup.find_all("a")
# print(links)
# print("\n")

# If we wanted to extract only the link that contains the text "About"
# on the page instead of every link, then we can use the built-in 
# "text" function to access the text content between the opening and closing a tags. <a> </a>
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])
