

import os
import sys


def get_size(dimension: str) -> int:
    """Return the terminal width or height."""

    try:
        terminal = os.get_terminal_size(sys.stdout.fileno())
        dimensions = {
            "width": terminal.columns,
            "height": terminal.lines,
        }

        if dimension not in dimensions:
            raise ValueError(
                "dimension must be 'width' or 'height'"
            )

        return dimensions[dimension]

    except OSError:
        if dimension == "width":
            return 80
        if dimension == "height":
            return 24
        raise ValueError(
            "dimension must be 'width' or 'height'"
        )
