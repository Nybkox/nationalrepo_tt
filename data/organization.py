import pathlib

import pandas as pd
from loguru import logger
import numpy as np


dp = pathlib.Path(__file__).parent.resolve()
df = pd.read_csv(dp.joinpath('articles.csv'))


organizations_df = df[['organization_code', 'organization_name']]
organizations_df = organizations_df.rename(columns={'organization_code': 'code', 'organization_name': 'name'})
_organizations_df2 = organizations_df.drop_duplicates(['name', 'code'])
organizations_df = organizations_df.drop_duplicates(['code'])

# detect different organizations with the same code
a = organizations_df
b = _organizations_df2
duplicates = (
    pd.merge(a, b, indicator=True, how="outer")
    .query('_merge=="right_only"')
    .drop("_merge", axis=1)
)

for _, row in duplicates.iterrows():
    row_code = row['code']
    row_name = row['name']
    used_name = organizations_df[organizations_df['code'] == row_code]['name'].iloc[0]
    logger.warning(
        f'An attempt to assign a new name ("{row_name}") for the organization with code {row_code}. The current name ("{used_name}") will be kept.'
    )

organizations_without_code = len(np.where(pd.isnull(organizations_df['code']))[0])
if organizations_without_code > 0:
    logger.warning(f'Found {organizations_without_code} organizations without code. They will not be imported.')
    organizations_df = organizations_df[pd.notnull(organizations_df['code'])]

organizations_df['id'] = np.arange(start=1, stop=len(organizations_df) + 1)
