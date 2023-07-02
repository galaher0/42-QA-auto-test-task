from playwright.sync_api import Page
from typing import NoReturn
import random
import re


class QuickStartRacePage:
    def __init__(self, page: Page) -> NoReturn:
        self.page = page
        self.page.set_viewport_size({"width": 1600, "height": 1200})
        self.visible_popup_element = page.locator("div[class*='popup']").locator("visible=true").first
        self.popup_close_btn = self.visible_popup_element.locator("input[type='button'][value='Закрыть']")

        self.race_text_area = page.locator("div[id='typetext']")
        self.text_input_field = page.locator("input[id='inputtext']")
        self.start_game_link = page.get_by_text("Начать игру")

        self.results_text = page.locator("div[class*='player you'] div[class='stats']")

    def close_popups_if_displayed(self) -> NoReturn:
        if self.visible_popup_element.is_visible():
            self.popup_close_btn.click()

    def start_game(self) -> NoReturn:
        if self.start_game_link.is_visible():
            self.start_game_link.click()
        self.race_text_area.wait_for()

    def read_and_prepare_race_text(self) -> list[str]:
        inner_text = (self.race_text_area.all_inner_texts())
        return inner_text[0].replace('o', 'о').replace('c', 'с').split()

    def type_a_word(self, word: str, delay: int = 100, with_error: bool = False) -> NoReturn:
        if with_error:
            self.text_input_field.type(chr(random.randrange(65, 123)), delay=delay)
            self.page.keyboard.press('Backspace')
        self.text_input_field.type(word, delay=delay)

    def select_random_words_by_count(self, words_len: int, percentage: int) -> list[int]:
        n_typos_to_make = round(words_len * percentage / 100) or 1
        return random.sample(list(range(words_len)), n_typos_to_make)

    def type_text(self, words: list[str], delay: int = 100, typos_percentage: int = 0) -> NoReturn:
        self.text_input_field.click()  # click waits until element is enabled
        sample = []
        if typos_percentage:
            sample = self.select_random_words_by_count(len(words), typos_percentage)
        for i, word in enumerate(words):
            if i in sample:
                self.type_a_word(word, delay=delay, with_error=True)
            else:
                self.type_a_word(word, delay=delay)
            self.page.keyboard.press('Space')

    def type_text_quickly_without_typos(self):
        text = self.read_and_prepare_race_text()
        self.type_text(text)

    def type_text_slowly_without_typos(self):
        text = self.read_and_prepare_race_text()
        self.type_text(text, delay=210)

    def type_text_quickly_with_typos(self):
        text = self.read_and_prepare_race_text()
        self.type_text(text, typos_percentage=random.randint(1, 7))

    def type_text_slowly_with_typos(self):
        text = self.read_and_prepare_race_text()
        self.type_text(text, delay=210, typos_percentage=random.randint(1, 7))

    def read_result(self) -> tuple[int, int]:
        self.results_text.click()
        search_regex = re.compile(r".+\.\d(\d+) зн\/мин(\d+) ошиб")
        results_string = (self.results_text.all_inner_texts())[0]
        speed, typos = re.search(search_regex, results_string).groups()
        return int(speed), int(typos)
