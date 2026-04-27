"""
Custom log output.
"""

import logging
import sys

TEXT_NORMAL = 0
TEXT_BOLD = 1
TEXT_RED = 31
TEXT_GREEN = 32
TEXT_YELLOW = 33
TEXT_BLUE = 34
TEXT_MAGENTA = 35
TEXT_CYAN = 36


def get_logger() -> logging.Logger:
    """Use this from all files needing to log."""
    pass


def setup_logger(debug: bool, color: bool) -> None:
    """Configure the logger."""
    pass


class Formatter(logging.Formatter):
    """
    Custom formatter, we like colors!
    """

    color: bool
    debug: bool

    def __init__(self, debug: bool = False, color: bool = False) -> None:
        self.color = color
        self.debug = debug
        if self.debug:
            log_format = "%(levelname)-6s %(message)s"
        else:
            log_format = "%(message)s"
        logging.Formatter.__init__(self, log_format)

    def format(self, record):
        pass


class Handler(logging.StreamHandler):
    """
    Custom StreamHandler so we can use the Formatter.
    """

    color: bool
    debug: bool

    def __init__(
        self, log_level: int, debug: bool = False, color: bool = False
    ) -> None:
        self.color = color
        self.debug = debug
        logging.StreamHandler.__init__(self, sys.stdout)
        self.setFormatter(Formatter(debug, color))
        self.setLevel(log_level)


#    def emit(self, record):
#        record.msg = "\x1b[%sm%s\x1b[%sm" % (TEXT_BOLD, record.msg, TEXT_NORMAL)
#        logging.StreamHandler.emit(self, record)
