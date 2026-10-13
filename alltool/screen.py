from .screenl.clearscr import clear_screen
from .screenl.terminal_size import get_size


def clear() -> None:
    clear_screen()


def size(pick: str) -> int:
    return get_size(pick)