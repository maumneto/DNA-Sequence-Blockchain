from LoadDataSet import *
from string import *
#def slideData():

def fitData():
    datasetOpening()
    arquivoDNA = open("dnaDATA.txt", "r")
    i = 0
    for row in arquivoDNA:
       print(row)
       print("O número de elementos concatenados é: " + str(len(row)))

    for element in row:
        i = i + 1
        if element == "|":
            print("O numero de elementos por subsetor é: " + str(i))
            break

    arquivoDNA.close()
