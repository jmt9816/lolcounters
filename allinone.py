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

while True:
    # Take user input for the champion's name and role
    champion_name = input("Enter the champion's name: ")
    role = input("Enter the role: ")

    # Filter the links to find the counters for the specified champion and role
    counter_links = [link for link in champion_links if champion_name.lower() in link and role.lower() in link and 'counters' in link]

    # If no counters are found, print an error and ask for input again
    if not counter_links:
        print(f"No counters found for {champion_name} ({role}). Please try again.")
        continue

    # Extract the counter champions from the links
    counter_champions = [link.split('=')[-1] for link in counter_links if link.split('=')[-1].lower() != champion_name.lower()]

    # Print the counter champions
    print(f'Here are the counter champions for {champion_name} ({role}):') 
    for counter in counter_champions:
        print(counter)
    break

# Close the browser
driver.quit()