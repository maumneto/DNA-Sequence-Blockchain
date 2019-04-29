import csv

def datasetOpening():
    with open('DNAsequenceDATASET.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        #print(csv_reader)
        cabecalho = True
        for row in csv_reader:
            if cabecalho:
                print(f'Nomes das colunas: {", ".join(row)}')
                cabecalho = False
            else:
                print(f'{", ".join(row)}')

if __name__ == '__main__':
    print("Olá")
    datasetOpening()
