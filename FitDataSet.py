from LoadDataSet import *
#def slideData():

def fitData():
    datasetOpening()
    arquivoDNA = open("dnaDATA.txt", "r")
    for row in arquivoDNA:
       print(row)

    arquivoDNA.close()
