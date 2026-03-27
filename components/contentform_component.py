from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.button_control import ButtonControl
from controls.input_control import InputControl


class Contentform(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator(".content_form"))

    def get_blue_button(self):
        return ButtonControl(self.page, self.wrapper.locator(".blue_button"))

    def click_by_blue_button(self):
        self.get_blue_button().click()

    def get_ddlYear(self):
        return InputControl(self.page, self.wrapper.locator('.select2-selection__rendered'))

    def get_innFl(self):
        return InputControl(self.page, self.wrapper.locator('[name="innFl"]'))

    def get_sum(self):
        return InputControl(self.page, self.wrapper.locator('[name="sum"]'))

    def click_ddlYear(self):
        self.get_ddlYear().click()

    def get_Year(self):
        return InputControl(self.page, self.wrapper.locator('.select2-search__field'))

    def fill_Year(self, title):
        self.get_Year().fill(title)

    def fill_innFl(self, title):
        self.get_innFl().fill(title)

    def fill_sum(self, title):
        self.get_sum().fill(title)

