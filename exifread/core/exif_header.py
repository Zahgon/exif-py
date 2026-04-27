"""
Base classes.
"""

import re
import struct
from typing import Any, BinaryIO, Dict, List, Optional, Tuple, Union

from exifread.core.exceptions import ExifError
from exifread.core.ifd_tag import IfdTag
from exifread.core.xmp import xmp_bytes_to_str
from exifread.exif_log import get_logger
from exifread.tags import (
    DEFAULT_STOP_TAG,
    IGNORE_TAGS,
    IfdDictValue,
    SubIfdTagDict,
    SubIfdTagDictValue,
)
from exifread.tags.exif import EXIF_TAGS
from exifread.tags.fields import (
    FIELD_DEFINITIONS,
    FLOAT_FIELD_TYPES,
    RATIO_FIELD_TYPES,
    SIGNED_FIELD_TYPES,
    FieldType,
)
from exifread.tags.makernote import (
    apple,
    canon,
    casio,
    dji,
    fujifilm,
    nikon,
    olympus,
    sony,
)
from exifread.utils import Ratio

logger = get_logger()


class ExifHeader:
    """
    Handle an EXIF header.
    """

    def __init__(
        self,
        file_handle: BinaryIO,
        endian: str,
        offset: int,
        fake_exif: int,
        strict: bool,
        debug=False,
        detailed=True,
        truncate_tags=True,
    ) -> None:
        self.file_handle = file_handle
        self.endian = endian
        self.offset = offset
        self.fake_exif = fake_exif
        self.strict = strict
        self.debug = debug
        self.detailed = detailed
        self.truncate_tags = truncate_tags
        self.tags: Dict[str, Any] = {}

    def s2n(self, offset: int, length: int, signed=False) -> int:
        """
        Convert slice to integer, based on sign and endian flags.

        Usually this offset is assumed to be relative to the beginning of the
        start of the EXIF information.
        For some cameras that use relative tags, this offset may be relative
        to some other starting point.
        """
        pass

    def n2b(self, offset: int, length: int) -> bytes:
        """Convert offset to bytes."""
        pass

    def _first_ifd(self) -> int:
        """Return first IFD."""
        pass

    def _next_ifd(self, ifd: int) -> int:
        """Return the pointer to next IFD."""
        pass

    def list_ifd(self) -> List[int]:
        """Return the list of IFDs in the header."""
        pass

    def _process_field(
        self,
        tag_name: str,
        count: int,
        field_type: int,
        type_length: int,
        offset: int,
    ) -> list:
        pass

    def _process_ascii_field(
        self, ifd_name: str, tag_name: str, count: int, offset: int
    ):
        pass

    def _get_printable_for_field(
        self,
        count: int,
        values: Union[str, list],
        field_type: FieldType,
        tag_entry: IfdDictValue,
        stop_tag: str,
    ) -> Tuple[str, bool]:
        # TODO: use only one type
        pass

    def _process_tag(
        self,
        ifd: int,
        ifd_name: str,
        tag_entry: SubIfdTagDictValue,
        entry: int,
        tag: int,
        tag_name: str,
        relative: bool,
        stop_tag: str,
    ) -> None:
        pass

    def dump_ifd(
        self,
        ifd: int,
        ifd_name: str,
        tag_dict=None,
        relative=0,
        stop_tag=DEFAULT_STOP_TAG,
    ) -> None:
        """Return a list of entries in the given IFD."""
        pass

    def extract_tiff_thumbnail(self, thumb_ifd: int) -> None:
        """
        Extract uncompressed TIFF thumbnail.

        Take advantage of the pre-existing layout in the thumbnail IFD as
        much as possible
        """
        pass

    def extract_jpeg_thumbnail(self) -> None:
        """
        Extract JPEG thumbnail.

        (Thankfully the JPEG data is stored as a unit.)
        """
        pass

    def decode_maker_note(self) -> None:
        """
        Decode all the camera-specific MakerNote formats

        Note is the data that comprises this MakerNote.
        The MakerNote will likely have pointers in it that point to other
        parts of the file. We'll use self.offset as the starting point for
        most of those pointers, since they are relative to the beginning
        of the file.
        If the MakerNote is in a newer format, it may use relative addressing
        within the MakerNote. In that case we'll use relative addresses for
        the pointers.
        As an aside: it's not just to be annoying that the manufacturers use
        relative offsets.  It's so that if the makernote has to be moved by the
        picture software all of the offsets don't have to be adjusted.  Overall,
        this is probably the right strategy for makernotes, though the spec is
        ambiguous.
        The spec does not appear to imagine that makernotes would
        follow EXIF format internally.  Once they did, it's ambiguous whether
        the offsets should be from the header at the start of all the EXIF info,
        or from the header at the start of the makernote.

        TODO: look into splitting this up
        """
        pass

    #    TODO Decode Olympus MakerNote tag based on offset within tag.
    #    def _olympus_decode_tag(self, value, mn_tags):
    #        pass

    def _canon_decode_tag(self, value, mn_tags: SubIfdTagDict) -> None:
        """
        Decode Canon MakerNote tag based on offset within tag.

        See http://www.burren.cx/david/canon.html by David Burren
        """
        pass

    def _canon_decode_camera_info(self, camera_info_tag: IfdTag) -> None:
        """
        Decode the variable length encoded camera info section.
        """
        pass

    def parse_xmp(self, xmp_bytes: bytes):
        """Adobe's Extensible Metadata Platform, just dump the pretty XML."""
        pass
