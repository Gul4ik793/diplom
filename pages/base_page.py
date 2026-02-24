from playwright.sync_api import Page


class BasePage:
    '''
            Базовая страница
    '''
    def __init__(self, page: Page, url: str):
        self.page: Page = page
        self.url: str = url

    def open(self):
        self.page.goto(self.url)