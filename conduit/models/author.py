from datetime import datetime as dt
from dataclasses import  dataclass

from conduit.database import (
    Model, Column, String, Boolean
)


@dataclass
class Author(Model):
    __tablename__ = 'authors'
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return self.name
