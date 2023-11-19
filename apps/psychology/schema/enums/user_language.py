# Standard Libraries
import enum

# Third-party Libraries
import strawberry


@strawberry.enum()
class LanguageEnum(enum.Enum):
    LANG_ES = strawberry.enum_value(value=1)
    LANG_EN = strawberry.enum_value(value=2)
    LANG_IT = strawberry.enum_value(value=3)
    LANG_GER = strawberry.enum_value(value=4)
    LANG_FR = strawberry.enum_value(value=5)


@strawberry.enum()
class LanguageLevelEnum(enum.Enum):
    LANG_LEVEL_EASY = strawberry.enum_value(value=1)
    LANG_LEVEL_MEDIUM = strawberry.enum_value(value=2)
    LANG_LEVEL_HARD = strawberry.enum_value(value=3)
    LANG_LEVEL_EXPERT = strawberry.enum_value(value=4)
