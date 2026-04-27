"""
Enable conversion of Exif IfdTags to native Python types
"""

from typing import Callable, Dict, List, Union

from exifread.core.exif_header import IfdTag
from exifread.exif_log import get_logger
from exifread.tags.fields import FieldType

logger = get_logger()

SerializedTagValue = Union[int, float, str, bytes, List[int], List[float], None]
SerializedTagDict = Dict[str, SerializedTagValue]


def convert_types(
    exif_tags: Dict[str, Union[IfdTag, bytes]],
) -> SerializedTagDict:
    """
    Convert Exif IfdTags to built-in Python types for easier serialization and programmatic use.

    - If the printable value of the IfdTag is relevant (e.g. enum type), it is preserved.
    - Otherwise, values are processed based on their field type, with some cleanups applied.
    - Single-element lists are unpacked to return the item directly.
    """
    pass


def convert_ascii(ifd_tag: IfdTag, tag_name: str) -> Union[str, bytes, None]:
    """
    Handle ASCII conversion, including special date formats.

    Returns:
    - str
    - bytes for rare ascii sequences that aren't Unicode
    - None for empty values
    """
    pass


def convert_undefined(ifd_tag: IfdTag, _tag_name: str) -> Union[bytes, str, int, None]:
    """
    Handle Undefined type conversion.

    Returns:
    - bytes if not Unicode such as Exif MakerNote
    - str for Unicode
    - int for rare MakerNote Tags containing a single value
    - None for empty values such as some MakerNote Tags
    """
    pass


def convert_numeric(ifd_tag: IfdTag, _tag_name: str) -> Union[int, List[int], None]:
    """
    Handle numeric types conversion.

    Returns:
    - int in most cases
    - list of int
    - None for empty values such as some MakerNote Tags

    Note: All Floating Point tags seen were empty.
    """
    pass


def convert_ratio(
    ifd_tag: IfdTag, _tag_name: str
) -> Union[int, float, List[int], List[float], None]:
    """
    Handle Ratio and Signed Ratio conversion.

    Returns:
    - int when the denominator is 1 or unused
    - float otherwise
    - a list of int or float, such as GPS Latitude/Longitude/TimeStamp
    - None for empty values such as some MakerNote Tags

    Ratios can be re-created with `Ratio(float_value).limit_denominator()`.
    """
    pass


def convert_bytes(ifd_tag: IfdTag, tag_name: str) -> Union[bytes, str, int, None]:
    """
    Handle Byte and Signed Byte conversion.

    Returns:
    - bytes
    - str for Unicode such as GPSVersionID and Image ApplicationNotes (XML)
    - int for single byte values such as GPSAltitudeRef or some MakerNote fields
    - None for empty values such as some MakerNote Tags
    """
    pass


def convert_proprietary(ifd_tag: IfdTag, _tag_name: str) -> Union[str, None]:
    """
    Handle Proprietary type conversion.

    Returns:
    - str as all tags of this made-up type (e.g. enums) prefer printable
    - None for very rare empty printable values
    """
    pass


# Mapping of field type to conversion function
conversion_map: Dict[FieldType, Callable] = {
    FieldType.PROPRIETARY: convert_proprietary,
    FieldType.BYTE: convert_bytes,
    FieldType.ASCII: convert_ascii,
    FieldType.SHORT: convert_numeric,
    FieldType.LONG: convert_numeric,
    FieldType.RATIO: convert_ratio,
    FieldType.SIGNED_BYTE: convert_numeric,
    FieldType.UNDEFINED: convert_undefined,
    FieldType.SIGNED_SHORT: convert_numeric,
    FieldType.SIGNED_LONG: convert_numeric,
    FieldType.SIGNED_RATIO: convert_ratio,
    FieldType.FLOAT_32: convert_numeric,
    FieldType.FLOAT_64: convert_numeric,
    FieldType.IFD: convert_bytes,
}
