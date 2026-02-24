from playwright.sync_api import Page

from components.auth_form_component import AuthForm
from pages.base_page import BasePage


class LKFL_Page(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "https://lkfl2.nalog.ru/lkfl/")

    def auth_form(self):
        return AuthForm(self.page)