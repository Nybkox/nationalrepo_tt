import pathlib

import pandas as pd
from loguru import logger
import numpy as np


dp = pathlib.Path(__file__).parent.resolve()
articles_df = pd.read_csv(dp.joinpath('articles.csv'))


articles_without_title = len(np.where(pd.isnull(articles_df['title']))[0])
if articles_without_title > 0:
    logger.warning(f'Found {articles_without_title} articles without title. They will not be imported.')
    articles_df = articles_df[pd.notnull(articles_df['title'])]

articles_without_organization = len(np.where(pd.isnull(articles_df['title']))[0])
if articles_without_title > 0:
    logger.warning(f'Found {articles_without_organization} articles without title. They will not be imported.')
    articles_df = articles_df[pd.notnull(articles_df['organization_code'])]

articles_without_author = len(np.where(pd.isnull(articles_df['authors']))[0])
if articles_without_author > 0:
    logger.warning(f'Found {articles_without_author} articles without authors.')

articles_without_funding = len(np.where(pd.isnull(articles_df['funding']))[0])
if articles_without_funding > 0:
    logger.warning(f'Found {articles_without_funding} articles without funding.')

articles_df['id'] = np.arange(start=1, stop=len(articles_df) + 1)
