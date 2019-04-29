import math
import LoadDataSet

def fitData():
    arquivoDNA = open("dnaDATA.txt", "r")
    for row in arquivoDNA:
        print(row)

if __name__ == '__main__':
    fitData()
