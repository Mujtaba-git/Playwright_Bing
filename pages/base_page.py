# pages/base_page.py

from playwright.sync_api import Page
from playwright._impl._api_types import TimeoutError


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url: str):

        # Standard Approach
        # self.page.goto(url)

        # Handling Timeout Errors

        # Solution 1
        # Due to slow internet getting timeout error so increasing the time
        # self.page.goto(url, timeout=60000)  # Increase to 60 seconds

        # Solution 2
        # self.page.goto(url, waitUntil = "networkidle")

        # Solution 3
        try:
            self.page.goto(url)
        except TimeoutError:
            print("Page load timed out. Retrying...")
            self.page.goto(url)
