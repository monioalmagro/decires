# Third-party Libraries
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

# Own Libraries
from apps.core import core_constants
from apps.psychology.models import UserAttachment
from config.enviroment_vars import settings


def get_url_default(gender: str) -> str:
    """
    Genera una URL para la imagen de perfil predeterminada basada en el género.
    """
    if int(gender) == core_constants.HOMBRE:
        gender_img = settings.DEFAULT_THUMBNAIL_MALE_IMAGE
    else:
        gender_img = settings.DEFAULT_THUMBNAIL_FEMALE_IMAGE

    return f"{settings.DECIRES_URL}{settings.STATIC_URL}{gender_img}"


def masked_img_resource(request: HttpRequest, **kwargs):
    """
    Vista para redirigir a un recurso enmascarado o a una imagen de
    perfil predeterminada.
    """
    pk = kwargs["pk"]
    gender = kwargs["gender"]
    if user_attachment := UserAttachment.objects.filter(
        id=pk,
        is_deleted=False,
        source_content_type=UserAttachment.USER_IMAGE,
    ).first():
        return redirect(user_attachment.url_path)

    return redirect(get_url_default(gender))


def masked_file_resource(request: HttpRequest, **kwargs):
    """
    Vista para redirigir a un recurso enmascarado o a una imagen de
    perfil predeterminada.
    """
    pk = kwargs["pk"]
    if (
        user_attachment := UserAttachment.objects.filter(
            id=pk,
            is_deleted=False,
        )
        .exclude(
            source_content_type=UserAttachment.USER_IMAGE,
        )
        .first()
    ):
        return redirect(user_attachment.url_path)
    return HttpResponse("")
