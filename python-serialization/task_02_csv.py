#!/usr/bin/env python3
"""
Define a function named convert_csv_to_json that takes the CSV
filename as its parameter and writes the JSON data to data.json
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    data = []
    try:
        with open(csv_filename, encoding="utf-8") as file:
            csvReader = csv.DictReader(file)

            for rows in csvReader:
                data.append(rows)

        json_filename = "data.json"
        with open(json_filename, "w", encoding="utf-8") as file:
            json.dump(data, file)
        return True

    except FileNotFoundError:
        print("File not found")
        return False


csv_filename = "data.csv"

convert_csv_to_json(csv_filename)
