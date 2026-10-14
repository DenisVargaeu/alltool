from .screenl.clearscr import clear_screen
from .screenl.terminal_size import get_size
from .screenl.title import sttitle

def clear() -> None:
    clear_screen()


def size(pick: str) -> int:
    return get_size(pick)

def set_title(name: str) -> int:
    sttitle(name)