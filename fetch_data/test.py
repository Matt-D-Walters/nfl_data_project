import pandas as pd
import nflreadpy as nfl

years = list(range(2015,2026))
team_data = nfl.load_team_stats(years)

team_data_pd = team_data.to_pandas()

# code to write the team data to a excel file
'''
team_data_pd.to_excel("nfl_data.xlsx", index=False)
'''

