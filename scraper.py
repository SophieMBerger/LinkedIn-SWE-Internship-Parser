from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Url to  fetch Software engineering internships in Vienna, Austria
URL = 'https://www.linkedin.com/jobs/search/?f_JT=I&geoId=107144641&keywords=software%20engineer&location=Vienna%2C%20Austria'

# Initiate the webDriver and get the URL contents
driver = webdriver.Chrome(ChromeDriverManager().install())
webpage = driver.get(URL)

# Get the html source code
html = driver.page_source
print(html)
