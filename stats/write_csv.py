import csv

def write_to_csv(data_file, qs):
    with open(data_file, "w+") as outfile:
        fields = ["bug", "time_spent_mins", "timestamp", "user"]
        writer = csv.DictWriter(outfile, fieldnames=fields)
        writer.writeheader()
        for obj in qs:
            writer.writerow(obj)