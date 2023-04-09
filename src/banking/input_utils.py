from typing import Callable

SHOULD_EXIT = True
EXIT = 0


def prompt_for_number(prompt_message: str) -> int:
    return int(input(prompt_message))


def menu(menu_msg: str, feature_dict: dict[int, Callable]):
    choice = prompt_for_number(menu_msg)
    while choice != EXIT:
        feature = feature_dict[choice]
        if feature() == SHOULD_EXIT:
            return
        choice = prompt_for_number(menu_msg)
    return SHOULD_EXIT
