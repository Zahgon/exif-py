"""Extract EXIF from JPEG files."""

from typing import BinaryIO, Tuple

from exifread.core.exceptions import InvalidExif
from exifread.core.utils import ord_
from exifread.exif_log import get_logger

logger = get_logger()


def _increment_base(data, base) -> int:
    pass


def _get_initial_base(fh: BinaryIO, data: bytes, fake_exif: int) -> Tuple[int, int]:
    pass


def _get_base(base: int, data: bytes) -> int:
    # pylint: disable=too-many-statements
    pass


def find_jpeg_exif(fh: BinaryIO, data: bytes, fake_exif: int) -> Tuple[int, bytes, int]:
    pass
