from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup WebDriver
def setup_driver():
    driver = webdriver.Chrome()  # adjust if you're using a different browser
    driver.get("http://localhost:3000/")
    return driver

# Helper function to close WebDriver
def teardown_driver(driver):
    driver.quit()

def test_view_all_movies():
    driver = setup_driver()
    try:
        movies = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
        )
        assert len(movies) > 0, "No movies were displayed on the home page"
        print("TC_WEB_001 passed")
    finally:
        teardown_driver(driver)

test_view_all_movies()

def test_search_complete_name():
    driver = setup_driver()
    try:
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "app-search-input"))
        )
        search_input.clear()
        complete_movie_name = "4 Kings 2"  # Replace with actual movie name
        search_input.send_keys(complete_movie_name)
        search_input.send_keys(Keys.RETURN)

        results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
        )
        assert len(results) > 0, "No matching movies found with complete name"
        
        # Additional check for matching titles
        for result in results:
            title = result.text  # Adjust if the title is stored in a different element
            assert complete_movie_name in title, f"Movie title '{title}' does not match search term '{complete_movie_name}'."

        print("TC_WEB_002 passed")
    finally:
        teardown_driver(driver)

test_search_complete_name()


def test_search_partial_name():
    driver = setup_driver()
    try:
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "app-search-input"))
        )
        search_input.clear()
        partial_movie_name = "4 Kings"  # Replace with actual partial name
        search_input.send_keys(partial_movie_name)
        search_input.send_keys(Keys.RETURN)

        results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
        )
        assert len(results) > 0, "No matching movies found with partial name"

        # Additional check for matching titles
        for result in results:
            title = result.text  # Adjust if the title is stored in a different element
            assert partial_movie_name in title, f"Movie title '{title}' does not match search term '{partial_movie_name}'."

        print("TC_WEB_003 passed")
    finally:
        teardown_driver(driver)

test_search_partial_name()


def test_search_non_existent_name():
    driver = setup_driver()
    try:
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "app-search-input"))  # Ensure class matches your HTML
        )
        search_input.clear()
        search_input.send_keys("Non-existent Movie Name")
        search_input.send_keys(Keys.RETURN)

        try:
            results = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
            )
            assert len(results) == 0, "Unexpected movies displayed for non-existent movie"
        except TimeoutException:
            print("No movies displayed, as expected for non-existent movie name.")
        
        print("TC_WEB_004 passed")
    finally:
        teardown_driver(driver)

test_search_non_existent_name()

def test_navigation_home_to_genre():
    driver = setup_driver()
    try:
        # Initially navigate to 'Search by genre page'
        driver.get("http://localhost:3000/genre")
        # Click on the 'Home' link to ensure it redirects back to the home page (assumed initial condition)
        home_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "homelink"))
        )
        home_link.click()
        # Verify we're redirected to the correct page
        assert "http://localhost:3000/" in driver.current_url, "Did not redirect to home page"
        print("TC_WEB_008 passed")
    finally:
        teardown_driver(driver)

def test_navigation_to_genre_page():
    driver = setup_driver()
    try:
        # Click on the 'Search by genre page' link
        genre_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "genrelink"))
        )
        genre_link.click()
        # Verify we're on the 'Search by genre page'
        assert "http://localhost:3000/genre" in driver.current_url, "Did not redirect to genre page"
        print("TC_WEB_009 passed")
    finally:
        teardown_driver(driver)

def test_navigation_to_age_page():
    driver = setup_driver()
    try:
        # Click on the 'Search by age page' link
        age_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "agelink"))
        )
        age_link.click()
        # Verify we're on the 'Search by age page'
        assert "http://localhost:3000/age" in driver.current_url, "Did not redirect to age page"
        print("TC_WEB_010 passed")
    finally:
        teardown_driver(driver)

# Run tests
test_navigation_home_to_genre()
test_navigation_to_genre_page()
test_navigation_to_age_page()

