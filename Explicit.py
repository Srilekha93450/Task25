import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the IMDb search page
URL = "https://www.imdb.com/search/name/"

# Function to generate random data for the search filters
def generate_random_data():
    # Random data generation
    random_name = "John Doe"  # Replace with actual random generation logic
    random_gender = random.choice(["male", "female"])
    random_birth_year = random.randint(1900, 2023)  # Example birth year range
    
    return random_name, random_gender, random_birth_year

# Function to perform IMDb search with random data
def perform_imdb_search():
    # Create a WebDriver instance (for Chrome in this case)
    driver = webdriver.Chrome()
    
    try:
        # Open the IMDb search page
        driver.get(URL)
        
        # Wait for the name input field to be visible and fill with random name
        name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
        random_name, random_gender, random_birth_year = generate_random_data()
        name_input.send_keys(random_name)
        
        # Select gender from dropdown
        gender_select = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "gender")))
        gender_select.click()
        gender_option = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#gender option[value='{random_gender}']")))
        gender_option.click()
        
        # Fill birth year in text field
        birth_year_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "birthYear")))
        birth_year_input.send_keys(str(random_birth_year))
        
        # Example: Click on Search button (adjust according to actual page behavior)
        search_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']")))
        search_button.click()
        
        # Wait for search results to load (example wait condition)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "findHeader")))
        
        # Print current URL (for verification)
        print("Search URL:", driver.current_url)
        
    finally:
        # Close the WebDriver session
        driver.quit()

# Execute the script
if __name__ == "__main__":
    perform_imdb_search()
