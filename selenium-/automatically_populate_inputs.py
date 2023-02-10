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

# Populate the inputs
username_input.send_keys("my_username")
email_input.send_keys("my_email@example.com")
password_input.send_keys("my_password")

# Find and click the submit button
submit_button = driver.find_element_by_id("submit")
submit_button.click()

# Close the browser window
driver.quit()
