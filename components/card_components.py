from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.input_control import InputControl


class Card(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator(".card-body.p-4"))

    def get_objectAddr(self):
        return InputControl(self.page, self.wrapper.locator('[name="objectAddr"]'))

    def get_li_locator(self, header_text: str):
        return self.page.locator(f"li:has-text('{header_text}')")

    def get_h2_locator(self, header_text: str):
        return self.page.locator(f"h2:has-text('{header_text}')")

    def get_h4_locator(self, header_text: str):
        return self.page.locator(f"h4:has-text('{header_text}')")