import pathlib
import pandas as pd
import numpy as np


dp = pathlib.Path(__file__).parent.resolve()
df = pd.read_csv(dp.joinpath('articles.csv'))
authors_df = df[['authors']]
authors_df = authors_df.rename(columns={'authors': 'name'})
authors_df['name'] = authors_df['name'].apply(lambda a: str(a).split(';'))
authors_df = authors_df.explode('name')
authors_df = authors_df.drop_duplicates()
authors_df = authors_df[pd.notnull(authors_df['name'])]

authors_df['id'] = np.arange(start=1, stop=len(authors_df) + 1)
