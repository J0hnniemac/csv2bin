#!/usr/bin/python
import sys
import csv
import struct
from pathlib import Path


def main(argv):
    print(argv[0])
    csvName = argv[0]
    with open(csvName) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            rowStr = ' db '
            for item in row:
                rowStr = rowStr + f"{item},"
            rowStr = rowStr[0:len(rowStr)-1]
            print(rowStr)


        print("-----------------")
    
    filename = Path(csvName)
    
    filename_bin = filename.with_suffix('.bin')
    f = open(filename_bin,'wb')
    with open(csvName) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in reader:
            rowStr = ' db '
            for item in row:
                a = int(item)
                single_byte = a.to_bytes(1, byteorder='big', signed=True)
                f.write(single_byte)  # Big-endian, unsigned int
    f.close()





if __name__ == "__main__":
   main(sys.argv[1:])

