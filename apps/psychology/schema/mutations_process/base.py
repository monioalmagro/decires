# Standard Libraries
from abc import ABC, abstractmethod

# Third-party Libraries
from strawberry.types import Info


class BaseMutationProcess(ABC):
    @abstractmethod
    async def validation_controller(self):
        pass

    @abstractmethod
    async def action(self, info: Info | None = None):
        pass
