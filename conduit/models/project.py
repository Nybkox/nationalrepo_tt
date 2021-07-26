from datetime import datetime as dt
from dataclasses import  dataclass

from conduit.database import (
    Model, Column, String
)


@dataclass
class Project(Model):
    __tablename__ = 'projects'

    code = Column(String(64), nullable=False, unique=True)
    provider = Column(String(128), nullable=True)
    name = Column(String(256), nullable=False)

    def __repr__(self) -> str:
        return self.name
