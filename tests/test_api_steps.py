import pytest
import requests
from playwright.sync_api import sync_playwright

# Define the API endpoint URL
api_url = "https://jsonplaceholder.typicode.com/posts/1"

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

def test_api_with_playwright(browser):
    # Make an HTTP GET request to the API using Playwright
    page = browser.new_page()
    page.goto(api_url)
    response_text = page.content()
    page.close()

    # Parse the response using the 'requests' library
    try:
        response = requests.get(api_url)
        api_data = response.json()

        # Perform assertions on the API response
        assert response.status_code == 200
        assert "userId" in api_data
        assert "title" in api_data
        assert "body" in api_data

    except requests.exceptions.RequestException as e:
        pytest.fail(f"API request failed: {e}")

    except ValueError as e:
        pytest.fail(f"Failed to parse API response as JSON: {e}")