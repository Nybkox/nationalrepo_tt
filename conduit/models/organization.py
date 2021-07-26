from dataclasses import  dataclass

from conduit.database import (
    Model, Column, String, Integer
)


@dataclass
class Organization(Model):
    __tablename__ = 'organizations'
    code = Column(Integer, unique=True, nullable=False)
    name = Column(String(128), nullable=True)

    def __repr__(self) -> str:
        return self.name
