HOMBRE = 1
MUJER = 2

GENDER_CHOICES = (
    (HOMBRE, "HOMBRE"),
    (MUJER, "MUJER"),
)

PRESENCIAL = 1
VIRTUAL = 2
DOMICILIO = 3


MODALITY_CHOICES = (
    (PRESENCIAL, "PRESENCIAL"),
    (VIRTUAL, "VIRTUAL"),
    (DOMICILIO, "DOMICILIO"),
)


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
