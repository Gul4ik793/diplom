from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.input_control import InputControl

class AuthForm(BaseComponent):
    def __init__(self, page: Page):
       super().__init__(page, page.locator('[data-qa="auth-form"]'))

    def get_username(self):
        return InputControl(self.page, self.wrapper.locator("#username_1"))

    def get_password(self):
        return InputControl(self.page, self.wrapper.locator("#password_2"))

    def fill_username(self, title):
        self.get_username().fill(title)

    def fill_password(self, title):
        self.get_password().fill(title)

    def get_buttons(self):
        return self.wrapper.locator("button")

    def click_by_text(self, text):
        self.wrapper.get_by_text(text, exact=True).click()

