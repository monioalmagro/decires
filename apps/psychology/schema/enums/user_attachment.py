# Standard Libraries
import enum

# Third-party Libraries
import strawberry

# Own Libraries
from apps.core import core_constants


@strawberry.enum()
class SourceAttachmentContentTypeEnum(enum.Enum):
    USER_IMAGE_PROFILE = strawberry.enum_value(value=core_constants.USER_IMAGE)
    USER_ATTACHMENT = strawberry.enum_value(value=core_constants.USER_ATTACHMENT)
