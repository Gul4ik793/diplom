from playwright.sync_api import Page

from components.contentform_component import Contentform
from controls.button_control import ButtonControl
from controls.input_control import InputControl
from pages.base_page import BasePage


class OPS_Page(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "https://www.nalog.gov.ru/rn02/service/ops/")

    def get_header_locator(self, header_text: str):
        return self.page.locator(f"h1:has-text('{header_text}')")

    def get_li_locator(self, header_text: str):
        return self.page.locator(f"li:has-text('{header_text}')")

    def get_contentform(self):
        return Contentform(self.page)

    def get_ddlYear(self):
        return InputControl(self.page, self.page.locator(".select2-search__field"))

    def click_unichk(self):
        ButtonControl(self.page, self.page.locator("#unichk_0")).click()

    def click_button(self):
        ButtonControl(self.page, self.page.locator("#btnContinue")).click()