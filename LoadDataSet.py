import csv

def datasetOpening():
    with open('DNAsequenceDATASET.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        cabecalho = True
        arquivo = open('dnaDATA.txt','w')
        for row in csv_reader:
            if cabecalho:
                print(f'Nomes das colunas: {", ".join(row)}')
                cabecalho = False
            else:
               arquivo.write(row[2].strip() + "\n")
        arquivo.close()

if __name__ == '__main__':
    datasetOpening()

