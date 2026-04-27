"""Utilities to find the EXIF offset and endian."""

import struct
from typing import BinaryIO, Dict, Tuple

from exifread.core.exceptions import ExifNotFound, InvalidExif
from exifread.core.heic import HEICExifFinder, find_heic_tiff
from exifread.core.jpeg import find_jpeg_exif
from exifread.core.jxl import JXLExifFinder
from exifread.core.utils import ord_
from exifread.exif_log import get_logger

logger = get_logger()


ENDIAN_TYPES: Dict[str, str] = {
    "I": "Intel",
    "M": "Motorola",
    "\x01": "Adobe Ducky",
    "b": "XMP/Adobe unknown",
}


def get_endian_str(endian_bytes) -> Tuple[str, str]:
    pass


def find_tiff_exif(fh: BinaryIO) -> Tuple[int, bytes]:
    pass


def find_webp_exif(fh: BinaryIO) -> Tuple[int, bytes]:
    pass


def find_png_exif(fh: BinaryIO, data: bytes) -> Tuple[int, bytes]:
    pass


def find_jxl_exif(fh: BinaryIO) -> Tuple[int, bytes]:
    pass


def determine_type(fh: BinaryIO) -> Tuple[int, bytes, int]:
    # by default do not fake an EXIF beginning
    pass
