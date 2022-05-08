import csv

rows = []

with open("main3.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)


planet_data_rows = rows[1:]

final_list = []
for star_data in planet_data_rows:
    temp_list = {
        "star_name":star_data[1],
        "distance":star_data[2],
        "mass":star_data[3],
        "radius":star_data[4],
        "gravity":star_data[5]
    }
    final_list.append(temp_list)

print(final_list)
