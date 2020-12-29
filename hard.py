#!/usr/bin/env python


"""
Read the main csv file, print and save the ranking of hard positions.


Setup:
  Install python 3.8 or newer


Requirements:
    numpy==1.19.4
    pandas==1.2.0
    python-dateutil==2.8.1
    pytz==2020.5
    six==1.15.0
    tabulate==0.8.7


Install requirements:
a) pip install -r requirements.txt

or

b) Intall below libraries individually
    pip install pandas
    pip install tabulate
"""


import pandas as pd
from tabulate import tabulate


def main():
    outfn = 'hard_talkchess_2020_hard_ranking.csv'

    infn = './docs/2020/hard_talkchess_2020_table.csv'
    df = pd.read_csv(infn)

    num_col = len(df.columns)

    # Add columns for count of engines that solved the positions and
    # the average time the solution is found for all engines.
    df['NumEngSolvedCount'] = df[list(df.columns[1:num_col])].count(axis=1)
    df['MeanTimeSec'] = round(df[list(df.columns[1:num_col])].mean(axis=1))
    # print(tabulate(df, headers='keys', tablefmt='psql', showindex=True))

    # Sort to get the ranking of hard positions.
    df_hard = df.sort_values(by=["NumEngSolvedCount", "MeanTimeSec"], ascending=[True, False])
    df_hard.reset_index(drop=True, inplace=True)

    # Print and save data frame on selected columns.
    df_hard_data = df_hard[['Solution', 'NumEngSolvedCount', 'MeanTimeSec']]

    # Print to screen.
    print('Hard:')
    print(tabulate(df_hard_data, headers='keys', tablefmt='psql', showindex=True))

    # Save to csv file on selected columns.
    df_hard_data.to_csv(outfn, index=False)


if __name__ == "__main__":
    main()
