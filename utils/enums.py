# Standard Libraries
import enum
from typing import TypeVar

TEnum = TypeVar("TEnum", bound=enum.Enum)


def get_enum_instance_by_value(
    enum_class: TEnum,
    value: int,
) -> TEnum | None:
    """
    Get an instance of an enumeration by its integer value.

    Args:
        enum_class (Type[TEnum]): The enumeration class.
        value (int): The integer value to match.

    Returns:
        TEnum | None: The enumeration instance if found, else None.
    """
    if match := next(iter(enum for enum in enum_class if enum.value == value), None):
        return match
    return None
