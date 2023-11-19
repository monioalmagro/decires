# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.models import UserLanguage
from apps.psychology.schema.enums.user_language import (
    LanguageEnum,
    LanguageLevelEnum,
)
from utils.enums import get_enum_instance_by_value


@strawberry.type()
class UserLanguageType:
    language_enum: LanguageEnum | None = None
    level_enum: LanguageLevelEnum | None = None

    @classmethod
    def from_db_model(cls, instance: UserLanguage) -> "UserLanguageType":
        return cls(
            language_enum=get_enum_instance_by_value(
                enum_class=LanguageEnum,
                value=instance.language,
            ),
            level_enum=get_enum_instance_by_value(
                enum_class=LanguageLevelEnum,
                value=instance.level,
            ),
        )
