from LoadDataSet import *

def fitData():
    datasetOpening()
    arquivoDNA = open("dnaDATA.txt", "r")
    for row in arquivoDNA:
       print(row)
    print("Number of elements: " + str(len(row)))

    #for element in row:
    #    i = i + 1
    #    if element == "|":
    #        print("Elements per line: " + str(i))
    #        break

    arquivoDNA.close()
