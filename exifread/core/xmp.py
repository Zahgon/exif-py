"""XMP related utilities.."""

from pyexpat import ExpatError
from typing import BinaryIO
from xml.dom.minidom import parseString

from exifread.exif_log import get_logger

logger = get_logger()


def find_xmp_data(fh: BinaryIO) -> bytes:
    pass


def xmp_bytes_to_str(xmp_bytes: bytes) -> str:
    """Adobe's Extensible Metadata Platform, just dump the pretty XML."""
    pass
