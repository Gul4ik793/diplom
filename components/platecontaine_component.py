from playwright.sync_api import Page

from components.base_component import BaseComponent


class Platecontaine(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator("#pnlSvcFl"))

    def get_by_text_block(self, text: str):
        return self.wrapper.get_by_text(text)

    def click_by_text(self, text):
        self.wrapper.get_by_text(text).click()
