import random
import string
from selenium import webdriver

# Define the URL of the page to load
url = "https://www.example.com/signup"

# Start a new instance of the Firefox driver
driver = webdriver.Firefox()

# Load the URL in the browser
driver.get(url)

# Find the elements for the inputs
username_input = driver.find_element_by_id("username")
email_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("password")

# Generate random strings for the username and password
username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

# Populate the inputs
username_input.send_keys(username)
email_input.send_keys(f"{username}@example.com")
password_input.send_keys(password)

# Find and click the submit button
submit_button = driver.find_element_by_id("submit")
submit_button.click()

# Close the browser window
driver.quit()
