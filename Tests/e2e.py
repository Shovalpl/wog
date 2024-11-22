from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import sys
import re


def test_scores_service(app_url):
    """
    Test the scores web service by:
    1. Opening the URL in a browser
    2. Finding the score element
    3. Checking if the score is a number between 1 and 1000

    Args:
        app_url (str): The URL of the scores application

    Returns:
        bool: True if the test passes, False otherwise
    """
    try:
        # Initialize Chrome in headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        # Open the URL
        driver.get(app_url)

        # Wait for the score element to be present
        wait = WebDriverWait(driver, 10)
        score_element = wait.until(
            EC.presence_of_element_located((By.ID, "score"))
        )

        # Get the score text
        score_text = score_element.text

        # Extract the number from the text using regex
        match = re.search(r'Current Score: (\d+)', score_text)

        if match:
            score = int(match.group(1))
            # Check if score is between 1 and 1000
            is_valid = 1 <= score <= 1000
        else:
            is_valid = False

        driver.quit()
        return is_valid

    except WebDriverException as e:
        print(f"Browser automation error: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False


def main_function():
    """
    Main function to run the tests

    Returns:
        int: 0 if tests pass, -1 if they fail
    """
    # You can modify this URL to match your application's address
    app_url = "http://localhost:5000"

    try:
        # Run the test
        result = test_scores_service(app_url)

        # Set exit code based on test result
        if result:
            print("Tests passed successfully!")
            return 0
        else:
            print("Tests failed!")
            return -1

    except Exception as e:
        print(f"Error running tests: {str(e)}")
        return -1


if __name__ == "__main__":
    # Run main function and exit with appropriate code
    sys.exit(main_function())