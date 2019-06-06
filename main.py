'''
'''
from FitDataSet import *
from storeDataJson import *

def main():

    fitData()
    data = storeData()

    for j in data:
        print(j)

if __name__ == "__main__":
    main()
