"""
Find Exif data in a JPEG XL file
"""

from typing import Tuple

from exifread.core.heic import HEICExifFinder


class JXLExifFinder(HEICExifFinder):
    """Find JPEG XL EXIF tags."""

    def find_exif(self) -> Tuple[int, bytes]:
        pass
