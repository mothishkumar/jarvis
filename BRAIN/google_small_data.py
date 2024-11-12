from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re

import undetected_chromedriver as uc

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

# Create a Chrome driver instance with the specified options
driver = webdriver.Chrome(options=chrome_options)


# Open Google in the browser
driver.get("https://www.google.com")

def search_brain(text):
    try:
        # Find the search box using its name attribute value
        search_box = driver.find_element("name", "q")

        # Clear the search box content
        search_box.clear()

        # Type the search query
        search_query = text
        search_box.send_keys(search_query)

        # Submit the form
        search_box.send_keys(Keys.RETURN)

        # Wait for a few seconds (you may need to adjust this based on your internet speed)
        driver.implicitly_wait(5)

        # Find the first search result element
        first_result = driver.find_element(By.CSS_SELECTOR, 'div.g')

        # Extract and print the first 3-4 sentences from the first search result, excluding links and dates
        first_result_text = first_result.text
        sentences = re.split(r'(?<=[.!?])\s', first_result_text)

        # Filter out sentences containing common link and date patterns
        filtered_sentences = [sentence for sentence in sentences if not re.search(r'https?://\S+|(\d{1,2} [A-Za-z]+ \d{10})', sentence)]

        # Join the remaining sentences
        result_text = '. '.join(filtered_sentences[:10])
        result_text = result_text.replace("Featured snippet from the web","")
        return result_text

    except Exception as e:
        print("An error occurred:", e)


