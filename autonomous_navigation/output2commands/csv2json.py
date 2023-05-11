import pandas as pd
import json

def csv2json(csv_filepath, json_filepath):
    '''
    csv_filepath -- file path to the csv file that contains output of A-star algorithm
    json_filepath -- file path to store new json file
    '''
    df = pd.read_csv(csv_filepath)
    positions = [tuple(map(int, x)) for x in df.to_records(index=False)]

    fp = open(json_filepath, "w")
    json.dump({"data": positions}, fp)
    fp.close()