#main.py 
from fetch_data.collecter import pull_pbp_data

if __name__ == '__main__':
    pbp_df = pull_pbp_data(list(range(2015,2024)))
    print(pbp_df.head())