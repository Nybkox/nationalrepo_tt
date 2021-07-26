import pathlib

import pandas as pd
import numpy as np
from loguru import logger


dp = pathlib.Path(__file__).parent.resolve()
projects_df = pd.read_csv(dp.joinpath('projects.csv'))
clear_projects_df = projects_df.drop_duplicates('code')
duplicates_count = projects_df.size - clear_projects_df.size

if duplicates_count > 0:
    logger.warning(f'Found {duplicates_count} projects with the same code. For each code, only the first line will be accepted.')

projects_df = clear_projects_df

projects_without_provider = len(np.where(pd.isnull(projects_df['provider']))[0])
if projects_without_provider > 0:
    logger.warning(f'Found {projects_without_provider} projects without provider.')

projects_without_name = len(np.where(pd.isnull(projects_df['name']))[0])
if projects_without_name > 0:
    logger.warning(f'Found {projects_without_name} projects without name. They will not be imported.')
    projects_df = projects_df[pd.notnull(projects_df['name'])]

projects_df['id'] = np.arange(start=1, stop=len(projects_df) + 1)
