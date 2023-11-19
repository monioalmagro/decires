# model AttentionModes

PRESENCIAL = 1
VIRTUAL = 2
DOMICILIO = 3

MODALITY_CHOICES = (
    (PRESENCIAL, "PRESENCIAL"),
    (VIRTUAL, "VIRTUAL"),
    (DOMICILIO, "DOMICILIO"),
)

# model UserAttachment
PREFIX_UNZIP = "unzip"
IMAGE_EXTENSIONS = {
    "image/jpeg": "jpg",
    "image/jpg": "jpg",
    "image/png": "png",
    "image/gif": "gif",
    "image/bmp": "bmp",
}
MEDIA_EXTENSIONS = {
    "application/pdf": "pdf",
    "application/zip": "zip",
    "application/x-compressed": "zip",
    "application/x-zip-compressed": "zip",
    "multipart/x-zip": "zip",
    "application/vnd.ms-powerpoint": "ppt",
    "application/msword": "doc",
    "video/mp4": "mp4",
    "application/octet-stream": "pbix",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
    "apadsheetml.sheet": "xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "xlsx",
    "application/vnd.ms-excel": "xls",
    "application/vnd.ms-excel.sheet.macroenabled.12": "xlsm",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "pptx",
    "application/x-rar-compressed": "rar",
    "application/rar": "rar",
}

# model OfficeLocation

VISIBILITY_DRAFT = 1
VISIBILITY_ACTIVE = 2
VISIBILITY_INACTIVE = 3

VISIBILITY_STATUS_CHOICES = (
    (VISIBILITY_DRAFT, "VISIBILITY_DRAFT"),
    (VISIBILITY_ACTIVE, "VISIBILITY_ACTIVE"),
    (VISIBILITY_INACTIVE, "VISIBILITY_INACTIVE"),
)

TYPE_HOUSE = 1
TYPE_OFFICE = 2
LOCATION_TYPE_CHOICES = (
    (TYPE_HOUSE, "TYPE_HOUSE"),
    (TYPE_OFFICE, "TYPE_OFFICE"),
)

# model UserCarreer

MODALITY_INDIVIDUAL = 1
MODALITY_GROUPS = 2

MODALITY_CHOICES = (
    (MODALITY_INDIVIDUAL, "MODALITY_INDIVIDUAL"),
    (MODALITY_GROUPS, "MODALITY_GROUPS"),
)

# model UserLanguage

LANG_ES = 1
LANG_EN = 2
LANG_IT = 3
LANG_GER = 4
LANG_FR = 5

LANG_CHOICES = (
    (LANG_ES, "LANG_ES"),
    (LANG_EN, "LANG_EN"),
    (LANG_IT, "LANG_IT"),
    (LANG_GER, "LANG_GER"),
    (LANG_FR, "LANG_FR"),
)

LANG_LEVEL_EASY = 1
LANG_LEVEL_MEDIUM = 2
LANG_LEVEL_HARD = 3
LANG_LEVEL_EXPERT = 4


LANG_LEVEL_CHOICES = (
    (LANG_LEVEL_EASY, "LANG_LEVEL_EASY"),
    (LANG_LEVEL_MEDIUM, "LANG_LEVEL_MEDIUM"),
    (LANG_LEVEL_HARD, "LANG_LEVEL_HARD"),
    (LANG_LEVEL_EXPERT, "LANG_LEVEL_EXPERT"),
)

# model
