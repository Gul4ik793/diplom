from playwright.sync_api import Page

from pages.base_page import BasePage
from components.content_center_component import ContentCenter


class EL_USL_Page(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "https://www.nalog.gov.ru/rn02/about_fts/el_usl/")

    def get_block(self):
        return ContentCenter(self.page)