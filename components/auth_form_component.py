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

    def get_error(self):
        return self.wrapper.locator('[data-qa="auth-error-msg"]')

    def get_button_by_text(self, text: str):
        return self.wrapper.get_by_text(text, exact=True)


