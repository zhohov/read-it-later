from src.core.shared.domain.entity import Entity


class Resource(Entity):
    def __init__(self, name: str, link: str) -> None:
        super().__init__()
        self.name = name
        self.link = link

