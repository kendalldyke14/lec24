#model.py
import csv

BB_FILE_NAME = 'umbball.csv'

bb_seasons = []

def init_bball(csv_file_name):
    with open(csv_file_name) as bballCsvFile:
        bballData = csv.reader(bballCsvFile)
        next(bballData) #throw away headers
        next(bballData) #throw away headers
        global bb_seasons
        bb_seasons = [] #reset, start clean
        for row in bballData:
            row[3] = int(row[3])
            row[4] = int(row[4])
            row[5] = float(row[5])
            bb_seasons.append(row)


def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
