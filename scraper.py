import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
# This is the executable path for linux. For Windows it will be different:
# driver = webdriver.Firefox(executable_path='c:\path\to\windows\webdriver\executable.exe')

driver.get('https://www.well.com/')

# Object is "results", brackets make the object an empty list.
# We will be storing our data here.
results = []

# Add the page source to the variable 'content'.
content = driver.page_source
# Load the contents of the page, its source, into BeautifulSoup
# class, which analyzes the HTML as a nested data structure and allows
# its elements by using various selctors.
soup = BeautifulSoup(content)
# Change 'list-item' to 'title'.
for element in soup.findAll(attrs={'class': 'title'}):
    name = element.find('a')
# Add the ibject of "name" to the list "results".
# '<element>.text' extracts the text in the element, omitting the HTML tags.
    results.append(name.text)

for x in results:
    print(x)
