import csv
from logging import error


def prepare_parse(file_with_path):
    data = []
    with open(file_with_path, 'r') as soubor:
        reader = csv.reader(soubor)
        for line in reader:
            data.append(line)
        return_data = {x: [] for x in data[0]}
        for line in data[1:]:
            for index, name in enumerate(data[0]):
                return_data[name].append(line[index])
        for name in return_data:
            if name in ("time", "Latitude", "Longtitude"):
                continue
            return_data[name] = [x for x in zip(return_data['time'], return_data[name]) if x[1]]
        return_data["position"] = zip(return_data['time'], return_data["Latitude"], return_data["Longtitude"])
        return return_data
