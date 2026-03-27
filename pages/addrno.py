from playwright.sync_api import Page

from components.card import Card
from pages.base_page import BasePage


class Addrno_Page(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "https://service.nalog.ru/addrno.do")

    def get_card(self):
        return Card(self.page)