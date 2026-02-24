from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.button_control import ButtonControl


class ContentCenter(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator(".list-block__item.js-filter-item"))

    def get_block(self):
        return ButtonControl(self.page, self.wrapper.locator(".list-title__text"))

    def get_by_text_block(self, text: str):
        return self.wrapper.get_by_text(text)

    def click_by_text(self, text):
        self.wrapper.get_by_text(text).click()
