# Standard Libraries
import json

# Third-party Libraries
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.utils import timezone

# Own Libraries
from config.enviroment_vars import settings


def javascript(request: HttpRequest):
    context = {}
    now = timezone.now()
    context["datetime"] = now.strftime("%d-%m-%YT%H:%M:%S%z")
    context["graphql_url"] = settings.GRAPHQL_URL
    context["site_name"] = settings.SITE_NAME
    context["select2_all"] = ""

    context["urls"] = {}
    context["urls"]["search"] = reverse("core:professional:search")

    var = "let Django = " + json.dumps(context, indent=2)
    return HttpResponse(var, content_type="application/javascript")
