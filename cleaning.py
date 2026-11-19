def parse_float(a):
    try:
        return float(a)
    except ValueError:
        return None
import csv
clean_rows = []
with open("raw_data.csv", "r", newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        t = parse_float(row['temp_c'])
        s = parse_float(row['sigma'])
        if t != None and s != None:
            clean_rows.append({'temp_c': t, 'sigma': s})

with open("clean_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['temp_c', 'sigma'], delimiter=';')
    writer.writeheader()
    writer.writerows(clean_rows)
    
    




