import csv
import math

def parse_float(value):
    try:
        return float(value)
    except ValueError:
        return None

def load_clean_data(a):
    clean_rows = []
    with open(a, 'r', newline="") as file:
        reader = csv.DictReader(file, delimiter = ';')
        for row in reader:
            t = parse_float(row['temp_c'])
            s = parse_float(row['sigma'])
            if t is not None and s is not None and s > 0:
                clean_rows.append({'temp_c': t, 'sigma': s})
    return clean_rows

def to_arrhenius_point(temp_c, sigma):
    temp_c = round(1000/(temp_c+273.15), 2)
    sigma = round(math.log10(sigma), 2)
    return (temp_c, sigma)




