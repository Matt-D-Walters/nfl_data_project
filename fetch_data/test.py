import pandas as pd
import nflreadpy as nfl
'''

years = list(range(2015,2026))
team_data = nfl.load_team_stats(years)

team_data_pd = team_data.to_pandas()
'''

# code to write the team data to a excel file
'''
team_data_pd.to_excel("nfl_data.xlsx", index=False)
'''

'''

nextgen = nfl.load_nextgen_stats()

nextgen_pd = nextgen.to_pandas()
nextgen_pd.to_excel("nextgen.xlsx", index=False)


players = nfl.load_ff_playerids()

players = players.to_pandas()
players.to_excel("players.xlsx", index=False)


'''

schedule = nfl.load_schedules(2025)
schedule = schedule.to_pandas()
schedule.to_excel("schedule.xlsx", index=False)