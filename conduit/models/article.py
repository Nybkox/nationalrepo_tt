from dataclasses import  dataclass

from conduit.database import (
    Model, Column, String, create_fk, relationship
)
from conduit.models.secondary import articles_authors, articles_fundings


@dataclass
class Article(Model):
    __tablename__ = 'articles'

    title = Column(String(128), nullable=False)
    authors = relationship('Author', secondary=articles_authors)
    funding = relationship('Project', secondary=articles_fundings)
    organization_id = create_fk('organizations')
    organization = relationship('Organization')
    
    def __repr__(self):
        return self.title
