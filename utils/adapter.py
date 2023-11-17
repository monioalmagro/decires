# Standard Libraries
from typing import List, Optional, Type, TypeVar

# Third-party Libraries
from django.db import models

# Own Libraries
from utils.database import async_database

ModelT = TypeVar("ModelT", bound=models.Model)
# Third-party Libraries
from django.db.models import QuerySet


class ModelAdapter:
    model_class: Type[ModelT] = None
    default_limit = 1000
    _log_tag = None

    @async_database()
    def get_object(self, **kwargs) -> Optional[ModelT]:
        instance = self.get_queryset(**kwargs)

        return instance.first() if instance.exists() else None

    def get_model_class(self) -> ModelT:
        if not self.model_class:
            raise NotImplementedError("Define model_class attr")
        return self.model_class

    def get_queryset(self, **kwargs) -> QuerySet[ModelT]:
        return self.get_model_class().objects.filter(**kwargs)

    @async_database()
    def get_objects(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        **kwargs,
    ) -> List[ModelT]:
        limit = limit or self.default_limit
        offset = offset or 0

        queryset = self.get_queryset(**kwargs)

        if order_by:
            queryset = queryset.order_by(*order_by)

        queryset = queryset[offset : offset + limit]

        return list(queryset)
