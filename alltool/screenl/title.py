def sttitle(name: str) -> None:
    """Set the terminal window title."""
    print(f"\033]0;{name}\007", end="", flush=True)