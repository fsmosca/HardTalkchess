#!/usr/bin/env python


"""
Extract the top epd hardest positions.


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


def get_epd(epdfn, pos_num):
    """
    Return epd based on indicated position number.
    """
    with open(epdfn) as f:
        for n, lines in enumerate(f):
            epd = lines.strip()
            if n + 1 == pos_num:
                return epd

    return None


def main():
    # Change this to 50 to get the hardest 50 positions
    num_top = 10

    epdfn = './docs/2020/hard_talkchess_2020.epd'
    outfn = f'top{num_top}_hard_positions.epd'

    infn = './docs/2020/hard_talkchess_2020_table.csv'
    df = pd.read_csv(infn)

    num_col = len(df.columns)
    df['NumEngSolvedCount'] = df[list(df.columns[1:num_col])].count(axis=1)
    df['MeanTimeSec'] = round(df[list(df.columns[1:num_col])].mean(axis=1))

    # Sort to get the ranking of hard positions.
    df_hard = df.sort_values(by=["NumEngSolvedCount", "MeanTimeSec"], ascending=[True, False])
    df_hard.reset_index(drop=True, inplace=True)

    solutions = df_hard['Solution'].to_list()

    with open(outfn, 'w') as f:
        for n, s in enumerate(solutions):
            pos_num = int(s.split()[0].split(')')[0])
            epd = get_epd(epdfn, pos_num)

            f.write(f'{epd}\n')

            if n + 1 >= num_top:
                break


if __name__ == "__main__":
    main()
