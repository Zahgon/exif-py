"""
Find Exif data in an HEIC file.

As of 2019, the latest standard seems to be "ISO/IEC 14496-12:2015"
There are many different related standards. (quicktime, mov, mp4, etc...)
See https://en.wikipedia.org/wiki/ISO_base_media_file_format for more details.

We parse just enough of the ISO format to locate the Exif data in the file.
Inside the 'meta' box are two directories we need:
  1) the 'iinf' box contains 'infe' records, we look for the item_id for 'Exif'.
  2) once we have the item_id, we find a matching entry in the 'iloc' box, which
     gives us position and size information.
"""

import struct
from typing import Any, BinaryIO, Callable, Dict, List, Optional, Tuple

from exifread.core.exceptions import ExifError, InvalidExif
from exifread.exif_log import get_logger

logger = get_logger()


def find_heic_tiff(fh: BinaryIO) -> Tuple[int, bytes]:
    """
    Look for TIFF header in HEIC files.

    In some HEIC files, the Exif offset is 0,
    and yet there is a plain TIFF header near end of the file.
    """
    pass


class BoxVersion(ExifError):
    """Wrong box version."""


class BadSize(ExifError):
    """Wrong box size."""


class Box:
    """A HEIC Box."""

    version = 0
    minor_version = 0
    item_count = 0
    size = 0
    after = 0
    pos = 0
    compat: List[bytes] = []
    base_offset = 0
    # this is full of boxes, but not in a predictable order.
    subs: Dict[str, "Box"] = {}
    locs: Dict = {}
    exif_infe: Optional["Box"] = None
    item_id = 0
    item_type = b""
    item_name = b""
    item_protection_index = 0
    major_brand = b""
    offset_size = 0
    length_size = 0
    base_offset_size = 0
    index_size = 0
    flags = 0
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return "<box '%s'>" % self.name

    def set_sizes(self, offset: int, length: int, base_offset: int, index: int) -> None:
        pass

    def set_full(self, vflags: int) -> None:
        """
        ISO boxes come in 'old' and 'full' variants.
        The 'full' variant contains version and flags information.
        """
        pass


class HEICExifFinder:
    """Find HEIC EXIF tags."""

    file_handle: BinaryIO

    def __init__(self, file_handle: BinaryIO) -> None:
        self.file_handle = file_handle

    def get(self, nbytes: int) -> bytes:
        pass

    def get16(self) -> int:
        pass

    def get32(self) -> int:
        pass

    def get64(self) -> int:
        pass

    def get_int4x2(self) -> tuple:
        pass

    def get_int(self, size: int) -> int:
        """some fields have variant-sized data."""
        pass

    def get_string(self) -> bytes:
        pass

    def next_box(self) -> Box:
        pass

    def get_full(self, box: Box) -> None:
        pass

    def skip(self, box: Box) -> None:
        pass

    def expect_parse(self, name: str) -> Box:
        pass

    def get_parser(self, box: Box) -> Optional[Callable[[Box], Any]]:
        pass

    def parse_box(self, box: Box) -> Box:
        pass

    def _parse_ftyp(self, box: Box) -> None:
        pass

    def _parse_meta(self, meta: Box) -> None:
        pass

    def _parse_infe(self, box: Box) -> None:
        pass
            # ignore the rest

    def _parse_iinf(self, box: Box) -> None:
        pass

    def _parse_iloc(self, box: Box) -> None:
        pass

    # Added a few box names, which as unhandled aborted data extraction:
    # hdlr, pitm, dinf, iprp, idat, iref
    #
    # Handling is initially `None`.
    # They were found in .heif photo files produced by Nokia 8.3 5G.
    #
    # They are part of the standard, referring to:
    #   - ISO/IEC 14496-12 fifth edition 2015-02-20 (chapter 8.10 Metadata)
    #     found in:
    #     https://mpeg.chiariglione.org/standards/mpeg-4/iso-base-media-file-format/text-isoiec-14496-12-5th-edition
    #     (The newest is ISO/IEC 14496-12:2022, but would cost 208 Swiss Francs at iso.org)
    #   - A C++ example: https://exiv2.org/book/#BMFF

    def _parse_hdlr(self, box: Box) -> None:
        pass

    def _parse_pitm(self, box: Box) -> None:
        pass

    def _parse_dinf(self, box: Box) -> None:
        pass

    def _parse_iprp(self, box: Box) -> None:
        pass

    def _parse_idat(self, box: Box) -> None:
        pass

    def _parse_iref(self, box: Box) -> None:
        pass

    def find_exif(self) -> Tuple[int, bytes]:
        pass
