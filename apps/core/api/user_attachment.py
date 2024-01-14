# Standard Libraries
import logging
from typing import Any

# Third-party Libraries
from django.core.files import File
from django.db import DatabaseError
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

# Own Libraries
from apps.psychology.models import UserAttachment

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class RegisterUserAttachment(TemplateView):
    http_method_names = ["post", "get"]

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.method.lower() == "post":
            return self.post(request=request, *args, **kwargs)
        return JsonResponse({"Error": "Method no allowed"})

    def save_file(self, request: HttpRequest, obj: UserAttachment):
        _file = request.FILES.get("attachment")
        update_fields = []
        if obj.content_type not in [".img", ".jpg", ".jpeg"]:
            obj.media_file.save(_file.name, File(_file))
            update_fields.append("media_file")
        else:
            obj.image.save(_file.name, File(_file))
            update_fields.append("image")

        obj.save(update_fields=update_fields)

    def saved_user_attachment(self, request: HttpRequest):
        data = request.POST
        _file = request.FILES.get("attachment")
        user_attachment = UserAttachment()
        user_attachment.description = data.get("description") or None
        user_attachment.source_content_type = data.get("source_type")
        user_attachment.name = _file.name
        user_attachment.content_type = f""".{File(_file).name.split(".")[-1]}"""
        user_attachment.size = _file.size / (1024 * 1024)
        user_attachment.url_path = "AWS PRESIGNED URL"
        user_attachment.save()
        return user_attachment

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # subir al bucket y guardar el path
        try:
            _files = request.FILES.get("attachment") or None

            if not _files:
                raise AssertionError("File not found in this request")

            attachment_instance = self.saved_user_attachment(request=request)
            self.save_file(request=request, obj=attachment_instance)

            return JsonResponse(
                {
                    "originalId": attachment_instance.pk,
                    "name": attachment_instance.name,
                    "attachment_path": attachment_instance.url_path,
                }
            )
        except AssertionError as exp:
            logger.warning(f"*** {self.__class__.__name__}.post ***")
            logger.warning(f"*** VALIDATION ERROR {repr(exp)} ***")
            return JsonResponse(
                {
                    "error": str(exp),
                    "type": "VALIDATION",
                    "code": 11,
                },
            )
        except DatabaseError as exp:
            logger.warning(f"*** {self.__class__.__name__}.post ***")
            logger.warning(f"*** INTEGRITY ERROR {repr(exp)} ***")
            return JsonResponse(
                {
                    "error": str(exp),
                    "type": "INTEGRITY",
                    "code": 12,
                },
            )
        except Exception as exp:
            logger.error(f"*** {self.__class__.__name__}.post ***")
            logger.error(f"*** INTERNAL ERROR {repr(exp)} ***")
            return JsonResponse(
                {
                    "error": str(exp),
                    "type": "INTERNAL",
                    "code": 13,
                },
            )
