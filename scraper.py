from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Url to  fetch Software engineering internships in Vienna, Austria
URL = 'https://www.linkedin.com/jobs/search/?f_JT=I&geoId=107144641&keywords=software%20engineer&location=Vienna%2C%20Austria'

# Initiate the webDriver and get the URL contents
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
# time.sleep(10)

# Get the html source code
html = driver.page_source
print(html)

# Create BeautifulSoup object and get unordered list of results element
soup = BeautifulSoup(html, 'html.parser')
resultsList = soup.find(
    "ul", class_="jobs-search__results-list")

# Get job postings
jobPostings = resultsList.find_all('a')

# Print out the company name of each job posting
for job in jobPostings:
    print(job.text)

# Close the driver
driver.close()
