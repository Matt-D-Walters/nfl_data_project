import nfl_data_py as nfl
import pandas as pd

def pull_pbp_data(years: list[int]) -> pd.DataFrame:
    '''
    # Pulls play-by-play data for each year provided in the input list.
    '''
    pdp_df = nfl.import_pbp_data(years, downcast=True, cache=False, alt_path=None)
    return pdp_df
    

