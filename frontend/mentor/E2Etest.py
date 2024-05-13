from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestMovieApp:
    def setup_driver(self):
        """Initialize the WebDriver."""
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/")
    
    def teardown_driver(self):
        """Close the WebDriver."""
        self.driver.quit()

    def test_view_all_movies(self):
        """Test if all movies are viewable."""
        self.setup_driver()
        try:
            movies = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
            )
            assert len(movies) > 0, "No movies were displayed on the home page"
            print("TC_WEB_001 passed")
        finally:
            self.teardown_driver()

    def test_search_complete_name(self):
        """Test searching by complete movie name."""
        self.setup_driver()
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "app-search-input"))
            )
            search_input.clear()
            complete_movie_name = "4 Kings 2"  # Replace with actual movie name
            search_input.send_keys(complete_movie_name)
            search_input.send_keys(Keys.RETURN)

            results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
            )
            assert len(results) > 0, "No matching movies found with complete name"
            for result in results:
                title = result.text
                assert complete_movie_name in title, f"Movie title '{title}' does not match search term '{complete_movie_name}'."
            print("TC_WEB_002 passed")
        finally:
            self.teardown_driver()

    def test_search_partial_name(self):
        """Test searching by partial movie name."""
        self.setup_driver()
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "app-search-input"))
            )
            search_input.clear()
            partial_movie_name = "4 Kings"  # Replace with actual partial name
            search_input.send_keys(partial_movie_name)
            search_input.send_keys(Keys.RETURN)

            results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
            )
            assert len(results) > 0, "No matching movies found with partial name"
            for result in results:
                title = result.text
                assert partial_movie_name in title, f"Movie title '{title}' does not match search term '{partial_movie_name}'."
            print("TC_WEB_003 passed")
        finally:
            self.teardown_driver()

    def test_search_non_existent_name(self):
        """Test searching for a non-existent movie name."""
        self.setup_driver()
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "app-search-input"))
            )
            search_input.clear()
            search_input.send_keys("Non-existent Movie Name")
            search_input.send_keys(Keys.RETURN)

            try:
                results = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
                )
                assert len(results) == 0, "Unexpected movies displayed for non-existent movie"
            except TimeoutException:
                print("No movies displayed, as expected for non-existent movie name.")
            print("TC_WEB_004 passed")
        finally:
            self.teardown_driver()

    def test_view_movie_detail(self):
        """Test that clicking on the first movie card shows basic detailed information about the movie."""
        self.setup_driver()
        try:
            # Click the first movie card
            first_movie_card = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child"))
            )
            first_movie_card.click()

            # Wait for the popup to become visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "popup"))
            )

            # Check the popup text content for key sections
            popup_text = self.driver.find_element(By.CLASS_NAME, "popup").text  # Get all text from the popup

            # Check if key sections are mentioned in the popup
            assert "Top Actors:" in popup_text, "Top Actors section is missing"
            assert "Genres:" in popup_text, "Genres section is missing"
            assert "Available Platform:" in popup_text, "Available Platforms section is missing"

            print("TC_WEB_005 passed")
        finally:
            self.teardown_driver()



    def test_filter_movies_by_genre(self):
        """Test that selecting a genre from the dropdown filters the movies accordingly."""
        self.setup_driver()
        try:
            self.driver.get("http://localhost:3000/genre") 
            genre_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "genre-select"))  # This matches the genre select dropdown
            )
            
            # Click to expand the dropdown
            genre_select.click()
            
            # Select a genre from the dropdown (e.g., Comedy)
            comedy_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//select[@class='genre-select']/option[@value='g002']"))
            )
            comedy_option.click()

            # Allow some time for the movie list to update based on the selected genre
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element(By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child").text != ""
            )

            # Verify the displayed movies are related to the selected genre (optional deeper validation could be added here)
            filtered_results = self.driver.find_elements(By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child") 
            assert len(filtered_results) > 0, "No movies displayed after selecting genre."
            print("TC_WEB_006 passed")
        finally:
            self.teardown_driver()


    def test_filter_movies_by_platform(self):
        """Test that selecting a platform filters the movies correctly."""
        self.setup_driver()
        try:
            self.driver.get("http://localhost:3000/platform")  # Navigate to the platform filter page

            # Find the platform dropdown element
            platform_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "platform-select"))
            )

            # Select a platform from the dropdown (e.g., Netflix)
            # Assuming the dropdown is using standard HTML select options
            from selenium.webdriver.support.ui import Select
            select = Select(platform_select)
            select.select_by_value('p003')  # Example value for Netflix

            # Allow some time for the movies to update based on the selected platform
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element(By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child").text != ""
            )

            # Verify the displayed movies are related to the selected platform
            filtered_results = self.driver.find_elements(By.CLASS_NAME, "css-46bh2p-MuiCardContent-root:last-child")
            assert len(filtered_results) > 0, "No movies displayed after selecting platform."
            print("TC_WEB_007 passed")
        finally:
            self.teardown_driver()


    def test_navigation_home(self):
        """Test navigation from the genre page back to the home page."""
        self.setup_driver()
        try:
            self.driver.get("http://localhost:3000/genre")
            home_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "homelink"))
            )
            home_link.click()
            assert "http://localhost:3000/" in self.driver.current_url, "Did not redirect to home page"
            print("TC_WEB_008 passed")
        finally:
            self.teardown_driver()

    def test_navigation_to_genre_page(self):
        """Test navigation to the genre search page."""
        self.setup_driver()
        try:
            genre_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "genrelink"))
            )
            genre_link.click()
            assert "http://localhost:3000/genre" in self.driver.current_url, "Did not redirect to genre page"
            print("TC_WEB_009 passed")
        finally:
            self.teardown_driver()

    def test_navigation_to_platform_page(self):
        """Test navigation to the platform search page."""
        self.setup_driver()
        try:
            age_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "platformlink"))
            )
            age_link.click()
            assert "http://localhost:3000/platform" in self.driver.current_url, "Did not redirect to platform page"
            print("TC_WEB_010 passed")
        finally:
            self.teardown_driver()

    def test_navigation_to_visualization_page(self):
        """Test navigation to the visualization page."""
        self.setup_driver()
        try:
            age_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "visuallink"))
            )
            age_link.click()
            assert "http://localhost:3000/visualization" in self.driver.current_url, "Did not redirect to platform page"
            print("TC_WEB_011 passed")
        finally:
            self.teardown_driver()



# Run tests
if __name__ == "__main__":
    test_suite = TestMovieApp()
    test_suite.test_view_all_movies()
    test_suite.test_search_complete_name()
    test_suite.test_search_partial_name()
    test_suite.test_search_non_existent_name()
    test_suite.test_view_movie_detail()
    test_suite.test_filter_movies_by_genre()
    test_suite.test_filter_movies_by_platform()
    test_suite.test_navigation_home()
    test_suite.test_navigation_to_genre_page()
    test_suite.test_navigation_to_platform_page()
    test_suite.test_navigation_to_visualization_page()
