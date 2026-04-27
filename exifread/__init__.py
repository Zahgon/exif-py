"""
Read Exif metadata from image files
Supported formats: TIFF, JPEG, PNG, Webp, HEIC
"""

from typing import Any, BinaryIO, Dict

from exifread.core.exceptions import ExifNotFound, InvalidExif
from exifread.core.exif_header import ExifHeader
from exifread.core.find_exif import determine_type, get_endian_str
from exifread.core.xmp import find_xmp_data
from exifread.exif_log import get_logger
from exifread.serialize import convert_types
from exifread.tags import DEFAULT_STOP_TAG

__version__ = "3.5.1"

logger = get_logger()


def _extract_xmp_data(hdr: ExifHeader, fh: BinaryIO):
    # Easy we already have them
    pass


def process_file(
    fh: BinaryIO,
    stop_tag: str = DEFAULT_STOP_TAG,
    details=True,
    strict=False,
    debug=False,
    truncate_tags=True,
    auto_seek=True,
    extract_thumbnail=True,
    builtin_types=False,
) -> Dict[str, Any]:
    """
    Process an image file to extract EXIF metadata.

    This is the function that has to deal with all the arbitrary nasty bits
    of the EXIF standard.

    :param fh: the file to process, must be opened in binary mode.
    :param stop_tag: Stop processing when the given tag is retrieved.
    :param details: If `True`, process MakerNotes.
    :param strict: If `True`, raise exceptions on errors.
    :param debug: Output debug information.
    :param truncate_tags: If `True`, truncate the `printable` tag output.
        There is no effect on tag `values`.
    :param auto_seek: If `True`, automatically `seek` to the start of the file.
    :param extract_thumbnail: If `True`, extract the JPEG thumbnail.
        The thumbnail is not always present in the EXIF metadata.
    :param builtin_types: If `True`, convert tags to standard Python types.

    :returns: A `dict` containing the EXIF metadata.
        The keys are a string in the format `"IFD_NAME TAG_NAME"`.
        If `builtin_types` is `False`, the value will be a `IfdTag` class, or bytes.
        IF `builtin_types` is `True`, the value will be a standard Python type.
    """
    pass
