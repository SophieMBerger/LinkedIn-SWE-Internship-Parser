import requests

# Fetch the LinkedIn webpage with software engineering internships in Vienna
URL = 'https://www.linkedin.com/jobs/search/?f_JT=I&geoId=107144641&keywords=software%20engineer&location=Vienna%2C%20Austria'
webpage = requests.get(URL)
print(webpage.content)
