#!/usr/bin/env python


"""
Read the main csv file, print and save the engine ranking by number of positions solved.


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
    outfn = 'hard_talkchess_2020_engine_ranking.csv'

    infn = './docs/2020/hard_talkchess_2020_table.csv'
    df = pd.read_csv(infn)

    # Define additional columns.
    full_header_list = list(df)
    header_list = full_header_list[1:]
    names, solves, mean_time_sec, pospermin, cpu, gpu, threads = [], [], [], [], [], [], []

    for h in header_list:
        name = h
        solve = df[h].count()
        mean_time = round(df[h].mean(axis=0))
        names.append(name)
        solves.append(solve)
        mean_time_sec.append(mean_time)

        if name == 'Lc0 v0.26.3 s1':
            pospermin.append(2)
            cpu.append('i7-2600K')
            threads.append(2)
            gpu.append('GTX 1650 super')
        elif name == 'Bluefish-FD-XI-DC':
            pospermin.append(5)
            cpu.append('AMD Ryzen Threadripper 3970X')
            threads.append(2)
            gpu.append('na')
        else:
            pospermin.append(30)
            cpu.append('i7-4930K')
            threads.append(1)
            gpu.append('na')

    data = {'name': names, 'numsolve': solves, 'meantimesec': mean_time_sec,
            'pospermin': pospermin, 'cpu': cpu, 'gpu': gpu, 'threads': threads}
    df_rank = pd.DataFrame(data)

    df_rank.sort_values('meantimesec', inplace=True, ascending=True)
    df_rank.sort_values('numsolve', inplace=True, ascending=False)
    df_rank.reset_index(drop=True, inplace=True)

    print(tabulate(df_rank, headers='keys', tablefmt='psql', showindex=True))

    df_rank.to_csv(outfn, index=False)


if __name__ == "__main__":
    main()
