import math
import numpy as np
from tabulate import tabulate
from astropy.table import Table

def sin(x):
    return np.sin(x)

x = np.linspace(0, 2 * math.pi, 1000)
y = sin(x)

# make table data
table_data = [(temp_x, temp_y) for temp_x, temp_y in zip(x,y)]

# create table with tabulate
table_header = ["x", "sin(x)"]

python_table = tabulate(table_data, headers=table_header)

def main():
    print(python_table)

if __name__ == "__main__":
    main()