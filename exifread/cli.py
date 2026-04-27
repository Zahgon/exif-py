#!/usr/bin/env python3
#
#
# Library to extract Exif information from digital camera image files.
# https://github.com/ianare/exif-py
#
#
# Copyright (c) 2002-2007 Gene Cash
# Copyright (c) 2007-2025 Ianaré Sévi and contributors
#
# See LICENSE.txt file for licensing information
# See ChangeLog.rst file for all contributors and changes
#

"""
Runs Exif tag extraction in command line.
"""

import argparse
import sys
import timeit

from exifread import __version__, exif_log, process_file
from exifread.core.exceptions import ExifError
from exifread.tags.fields import FIELD_DEFINITIONS

logger = exif_log.get_logger()


def get_args() -> argparse.Namespace:
    pass


def run_cli(args: argparse.Namespace) -> None:
    """Extract tags based on options (args)."""
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
