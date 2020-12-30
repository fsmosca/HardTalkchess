#!/usr/bin/env python


"""
Read arena report file and append the result to the old data table.


Setup:
  Install python 3.8 or newer


Requirements:
    numpy==1.19.3
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


usage:
python arena_report_parser.py test_result.rep.
"""


import sys

import pandas as pd


def read_arena_report(fn):
    """
    Read arena report file with file extension .rep.
    """
    start = False
    timesec, solutions = [], []
    engine_name = None

    with open(fn) as f:
        for lines in f:
            line = lines.strip()

            # Get engine name
            if 'Analyzing engine: ' in line:
                engine_name = line.split('Analyzing engine: ')[1]
                continue

            if 'Activate abort analysis' in line and not start:
                start = True
                continue

            if start and ')' in line:
                sp = line.split('*')
                sol = ' '.join(sp[0].split()[0:-1])
                solutions.append(sol)
                if len(sp) < 2:
                    timesec.append(None)
                    continue

                solve_time_sec = int(sp[1].strip().split('Sec')[0].strip())
                timesec.append(solve_time_sec)

    d = {'Solution': solutions, engine_name: timesec}
    df = pd.DataFrame(d)

    return df[engine_name].to_list(), engine_name


def main(argv):
    if len(argv) == 0:
        print('Error, arena report file is missing.')
        print('usage: python arena_report_parser.py arena_result.rep')
        return

    outfn = 'new_hard_talkchess_2020_table.csv'

    # The file where new data will be added.
    existingfn = './docs/2020/hard_talkchess_2020_table.csv'

    # Convert the new result from arena report file, into a list.
    infn = argv[0]
    data_list, name = read_arena_report(infn)

    # Append the new result from arena report file
    # into the main table hard_talkchess_2020_table.csv.
    df = pd.read_csv(existingfn)
    df[name] = data_list

    # Save to csv file the updated table to new_hard_talkchess_2020_table.csv
    df.to_csv(outfn, index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
