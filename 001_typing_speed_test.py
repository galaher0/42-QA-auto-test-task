from models.main_page import MainPage
from models.quickstart_race_page import QuickStartRacePage
from playwright.sync_api import Page
import pytest


@pytest.fixture(params=['type_text_quickly_without_typos',
                        'type_text_slowly_without_typos',
                        'type_text_quickly_with_typos',
                        'type_text_slowly_with_typos'])
def play_game_in_four_cases(page: Page, request):
    main_page = MainPage(page)
    race_page = QuickStartRacePage(page)

    main_page.navigate()
    main_page.quick_start()

    race_page.close_popups_if_displayed()
    race_page.start_game()

    getattr(race_page, request.param)()

    race_page.close_popups_if_displayed()

    return race_page


def test_speed_and_typos(play_game_in_four_cases):
    race_page = play_game_in_four_cases
    errors = []

    speed, typos = race_page.read_result()

    test_result_msg = f"Скорость набора: {speed} зн/мин, {typos} ошибок"

    print('\n', test_result_msg, sep='')

    if not (speed > 400):
        errors.append("Скорость набора должна быть больше 400 зн/мин")
    if not (typos == 0):
        errors.append("Ошибок быть не должно")

    assert not errors, f"{test_result_msg}. {', '.join(errors)}"
