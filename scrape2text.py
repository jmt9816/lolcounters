from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import time

URL = "https://www.op.gg/champions"

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(service=Service(r'C:\Users\jorda\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe'))
driver.minimize_window()
# Go to the URL
driver.get(URL)

# Wait for the dynamically loaded elements to show up
time.sleep(5)

# Parse the HTML of the page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all 'a' tags with href containing 'champions'
a_tags = soup.find_all('a', href=True)
champion_links = [tag['href'] for tag in a_tags if 'champions' in tag['href']]

# Open the file in write mode
with open('output.txt', 'w') as f:
    # Write all the links to the file
    for link in champion_links:
        # Check if the link ends with '/build'
        if not link.endswith('/build'):
            f.write(link + '\n')

# Close the browser
print("Done!")
driver.quit()