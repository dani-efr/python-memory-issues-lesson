import csv
import json


def convert():
    # read the raw_data.json file and convert it to a simple readable table
    headers = ["Row Number", "State", "Measure", "Value"]

    with open("data/data.json", "r") as f:
        raw_data = json.load(f)

    with open("data/result.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i, line in enumerate(raw_data.get("data")):
            row_number = i+1
            state = line[9]
            measure = line[13]
            value = line[14]
            row = [row_number, state, measure, value]
            writer.writerow(row)

