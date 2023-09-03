# tests/test_bing_maps.py

import unittest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage


class BingMapsTest(unittest.TestCase):

    def setUp(self):
        self.playwright = sync_playwright().start()

        # Headless
        self.browser = self.playwright.chromium.launch()

        # Without Headless
        # self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.home = HomePage(self.page)
        self.home.go_to("https://www.bing.com/maps/")

    def test_page_title(self):
        self.assertEqual(self.home.page_title, "Bing Maps - Directions, trip planning, traffic cameras & more")

    def test_directions_button(self):
        self.assertTrue(self.home.get_directions_button.is_visible())

    def test_search_bar(self):
        self.assertTrue(self.home.search_bar.is_visible())

    def test_map_loads(self):
        self.assertTrue(self.home.map_loaded())

    def test_road_view(self):
        self.assertTrue(self.home.road_view_available())

    def tearDown(self):
        self.browser.close()
        self.playwright.stop()


if __name__ == "__main__":
    unittest.main()
