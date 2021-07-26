from loguru import logger
import pandas as pd
from conduit.app import create_app, db


def main():
    app = create_app()

    # it should be imported after app's logger is configured
    from data.articles import articles_df
    from data.organization import organizations_df
    from data.authors import authors_df
    from data.projects import projects_df

    with app.app_context():
        db.drop_all()
        logger.debug('Database cleared.')
        
        db.create_all()
        logger.debug(f'Database tables ({list(db.metadata.tables.keys())}) created.')
        
        # projects
        projects_df.to_sql('projects', con=db.engine, if_exists='append', index=False)
        projects_df = projects_df.rename(columns={'id': 'project_id'})
        logger.debug(f'{len(projects_df)} projects imported.')

        # organization
        organizations_df.to_sql('organizations', con=db.engine, if_exists='append', index=False)
        organizations_df = organizations_df.rename(columns={'id': 'organization_id'})
        logger.debug(f'{len(organizations_df)} organizations imported.')

        # authors
        authors_df.to_sql('authors', con=db.engine, if_exists='append', index=False)
        authors_df = authors_df.rename(columns={'id': 'author_id'})
        logger.debug(f'{len(authors_df)} authors imported.')

        # articles
        articles_df = pd.merge(articles_df, organizations_df, left_on='organization_code', right_on='code')
        articles_df = articles_df.drop(['code', 'name', 'organization_code', 'organization_name'], axis=1)
        wrtiable_articles_df = articles_df.drop(['funding', 'authors'], axis=1)
        wrtiable_articles_df.to_sql('articles', con=db.engine, if_exists='append', index=False)
        articles_df = articles_df.rename(columns={'id': 'article_id'})
        logger.debug(f'{len(wrtiable_articles_df)} articles imported.')

        # remove unnecessary data for secondary tables
        articles_df = articles_df.drop(['title', 'organization_id'], axis=1)

        # associative table for Article - Author relationship
        articles_authors_df = articles_df.copy()
        articles_authors_df['authors'] = articles_authors_df['authors'].apply(lambda a: str(a).split(';'))
        articles_authors_df = articles_authors_df.explode('authors')
        articles_authors_df = pd.merge(articles_authors_df, authors_df, left_on='authors', right_on='name')
        articles_authors_df = articles_authors_df.drop(['name', 'authors', 'funding'], axis=1)
        articles_authors_df = articles_authors_df.drop_duplicates()
        articles_authors_df.to_sql('articles_authors', con=db.engine, if_exists='append', index=False)
        logger.debug(f'{len(articles_authors_df)} Article - Author relationships created.')
        
        # associative table for Article - Project relationship
        articles_fundings_df = articles_df.copy()
        articles_fundings_df['funding'] = articles_fundings_df['funding'].apply(lambda a: str(a).split(','))
        articles_fundings_df = articles_fundings_df.explode('funding')
        articles_fundings_df = pd.merge(articles_fundings_df, projects_df, left_on='funding', right_on='code')
        articles_fundings_df = articles_fundings_df.drop(['funding', 'code', 'provider', 'name', 'authors'], axis=1)
        articles_fundings_df = articles_fundings_df.drop_duplicates()
        articles_fundings_df.to_sql('articles_fundings', con=db.engine, if_exists='append', index=False)
        logger.debug(f'{len(articles_fundings_df)} Article - Project relationships created.')


if __name__ == '__main__':
    main()
