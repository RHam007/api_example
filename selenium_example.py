from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Simple Selenium script to explore usage of the library, and was originally provided as part of the
MicroSoft Web Development with Python course, via Coursera.  Any cusomization by myself, will be marked using in-line comments.

This script assumes installation of selenium (pip install selenium), and installation of the WebDriver for your browser of choice.
WebDrivers, Selenium documentation, and other resources can be found on the official website (www.selenium.dev)
"""
# Initialize the WebDriver (replace with the path to your WebDriver)
driver = webdriver.Chrome('/path/to/chromedriver')

# Navigate to a website
driver.get('https://www.example.com') # Website for testing

# Find an element by its ID and interact with it
search_box = driver.find_element(By.ID, 'search-input')
search_box.send_keys('Selenium automation')
search_box.submit()

# Close the browser
driver.quit()