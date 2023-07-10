from playwright.sync_api import Page
from typing import NoReturn


class MainPage:
    def __init__(self, page: Page) -> NoReturn:
        self.page = page
        self.page.set_viewport_size({"width": 1600, "height": 1200})
        self.quick_start_link = page.get_by_text("Быстрый старт")

    def navigate(self) -> NoReturn:
        self.page.goto("/")

    def quick_start(self) -> NoReturn:
        self.quick_start_link.click()
        self.page.wait_for_load_state()
