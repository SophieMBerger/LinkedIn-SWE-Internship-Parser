import string
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(
    description="Search for SWE internships in any location")
parser.add_argument(
    "location", help="the location to search or SWE internships in")
args = parser.parse_args()

# Location (Country/City/State) in which to search for SWE internships
location = args.location

# Url to  fetch Software engineering internships in selected country
URL = f'https://www.linkedin.com/jobs/search/?f_JT=I&keywords=software%20engineer&location={location}'

# Initiate the webDriver and get the URL contents
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
# time.sleep(10)

# Get the html source code
html = driver.page_source

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
