from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.button_control import ButtonControl


class Headermenu(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator(".header-menu"))

    def get_headermenu(self):
        return ButtonControl(self.page, self.wrapper.locator(".header-menu__link"))

    def click_by_text_text(self, text: str):
        return self.wrapper.get_by_text(text).click()
