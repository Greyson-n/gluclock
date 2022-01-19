import datetime
import json


filepath = "/home/runner/dexcomparser/test.json"

def parse_date_for_hour(date_string):
    dt = datetime.datetime.strptime("2018-02-06T01:07:35", "%Y-%m-%dT%H:%M:%S")
    print(dt.second)
    return dt.hour

def main():
    # Initialize data list with empty list at each hour
    egvs_by_hour = [[] for _ in range(24)]
    with open(filepath) as json_file:
        data = json.load(json_file)
        print(data.keys())






if __name__ == "__main__":
    # main()
    assert parse_date_for_hour("2018-02-06T01:07:35") == 1

