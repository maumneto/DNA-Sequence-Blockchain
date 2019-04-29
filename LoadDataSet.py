import csv

def datasetOpening():
    with open(DNAsequenceDATASET.csv) as csv_file:
        csv_reader = csv.reader(csv_file)
        cabecalho = False
        print(csv_reader)

if __name__ == '__main__':
    print("Olá")
    datasetOpening()
