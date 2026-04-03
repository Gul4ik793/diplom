from playwright.sync_api import Page

from components.base_component import BaseComponent


class Headermenu(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator(".header-menu"))

    def get_by_text(self, text: str):
        return self.wrapper.get_by_text(text)
