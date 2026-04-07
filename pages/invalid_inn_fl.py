from playwright.sync_api import Page

from controls.button_control import ButtonControl
from controls.input_control import InputControl
from pages.base_page import BasePage


class Invalidinnfl_Page(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "https://service.nalog.ru/invalid-inn-fl.html")

    def get_inn(self):
        return InputControl(self.page, self.page.locator("#inn"))

    def get_btn_with_icon_search(self):
        return ButtonControl(self.page, self.page.locator(".btn-with-icon.btn-search"))

    def det_Result(self):
        return self.page.locator(".msg-no-data")
