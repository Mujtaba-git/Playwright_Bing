# pages/home_page.py

from pages.base_page import BasePage


class HomePage(BasePage):

    @property
    def page_title(self):
        return self.page.title()

    @property
    def get_directions_button(self):
        return self.page.locator(
            ".directionsIcon")  # This selector is hypothetical; you need to find the actual selector from the Bing Maps page.

    @property
    def search_bar(self):
        return self.page.locator("#maps_sb")  # This selector is hypothetical.

    def map_loaded(self):
        # Check if some map element or attribute is present.
        return self.page.locator("#map-element").is_visible()  # This selector is hypothetical.

    #def road_view_available(self):
        #return self.page.locator("#road-view-option").is_visible()  # This selector is hypothetical.

    def road_view_available(self):
        return self.page.locator('button img[alt="Road"]').is_visible()


