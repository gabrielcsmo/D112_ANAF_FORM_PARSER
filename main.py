#!/usr/bin/env python3

import sys
import os
import camelot
import pandas as pd

NCOLS = 11
sums = [0] * 11

def main():
    input_fname = sys.argv[1]
    tables = camelot.read_pdf(input_fname, pages='1-end')
    out_file = open(input_fname + ".csv", 'w+')

    result = {}
    for table in tables:
        dft = table.df
        #vals = dft[0].values
        for i in range(NCOLS):
            if i not in result:
                result[i] = list(dft[i].values)
            else:
                result[i].extend(list(dft[i].values))
    #print(result)
    entries = len(result[0])

    for j in range(entries):
        """skip the headers except first"""
        if j > 0 and result[0][j] == result[0][0]:
            continue

        rr = result[0][j].replace('\n', '').replace('\r','').strip()
        for i in range(1, 11):
            rr += "; " + result[i][j].replace('\n', ' ').replace('\r',' ').strip()
            if i > 5 and j > 0:
                sums[i] += int(result[i][j].strip())
        out_file.write(rr + '\n')
    out_file.write(" ;" * 10 + "\n")
    out_file.write(" ;" * 10 + "\n")
    out_file.write("Total" + " ;" * 10 + "\n")
    out_file.write("; ".join([str(s) for s in sums]))
    out_file.close()
    print("Saved the csv in: {}".format(input_fname + ".csv"))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 {} <{}>".format(sys.argv[0], "d112.pdf"))
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print("File {} does not exists".format(sys.argv[1]))
        sys.exit(1)

    main()
