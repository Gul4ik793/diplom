from playwright.sync_api import Page

from components.base_component import BaseComponent


class ContentCenter(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator(".list-block__item.js-filter-item"))

    def get_by_text_block(self, text: str):
        return self.wrapper.get_by_text(text)