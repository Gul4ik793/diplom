from playwright.sync_api import Page

from pages.base_page import BasePage
from components.header_menu_component import Headermenu

class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "https://www.nalog.gov.ru/rn02/")

    def get_headermenu(self):
        return Headermenu(self.page)
