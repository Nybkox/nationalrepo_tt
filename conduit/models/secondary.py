from conduit.database import Table, create_fk


articles_authors = Table('articles_authors', 
    create_fk('authors', primary_key=True, name='author_id'),
    create_fk('articles', primary_key=True, name='article_id')
)

articles_fundings = Table('articles_fundings', 
    create_fk('projects', primary_key=True, name='project_id'),
    create_fk('articles', primary_key=True, name='article_id')
)
