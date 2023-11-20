# Standard Libraries
import enum

# Third-party Libraries
import strawberry


@strawberry.enum()
class LanguageEnum(enum.Enum):
    ES = strawberry.enum_value(value=1)
    EN = strawberry.enum_value(value=2)
    IT = strawberry.enum_value(value=3)
    GER = strawberry.enum_value(value=4)
    FR = strawberry.enum_value(value=5)


@strawberry.enum()
class LanguageLevelEnum(enum.Enum):
    EASY = strawberry.enum_value(value=1)
    MEDIUM = strawberry.enum_value(value=2)
    HARD = strawberry.enum_value(value=3)
    EXPERT = strawberry.enum_value(value=4)
