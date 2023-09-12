import pytest
import os
import glob
import json
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

# Read the configuration from the JSON file
config = json.load(open('C:\\Playwright_python\\config.json'))


@pytest.fixture(scope="function", params=config.keys())
def browser_type(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(**config[request.param])
        yield browser
        browser.close()


# Fixture for video recording
@pytest.fixture(scope="function")
def page(browser_type, request):
    video_path = f"C:\\Playwright_python\\videos\\{request.node.name}.webm"

    # context = browser_type.new_context(
    context = browser_type.new_context(
        # record_video_dir='C:\\Playwright_python\\videos',  # Update the path where you want to store the videos
        record_video_dir=os.path.dirname(video_path),
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()

    # Rename the video file to match the test case name
    # Assume that the generated video is the newest .webm file in the directory
    list_of_files = glob.glob(os.path.dirname(video_path) + '/*.webm')
    latest_file = max(list_of_files, key=os.path.getctime)
    os.rename(latest_file, video_path)


@pytest.fixture(scope="function")
def home_page(page):
    home = HomePage(page)
    home.go_to("https://www.bing.com/maps/")
    return home


def test_page_title(home_page):
    assert home_page.page_title == "Bing Maps - Directions, trip planning, traffic cameras & more"


def test_directions_button(home_page):
    assert home_page.get_directions_button.is_visible


def test_search_bar(home_page):
    assert home_page.search_bar.is_visible


# def test_map_loads(home_page):
#     assert home_page.map_loaded


def test_road_view(home_page):
    assert home_page.road_view_available

# def tearDown(self):
#     self.browser.close()
#     self.playwright.stop()
#
#
# if __name__ == "__main__":
#     unittest.main()
