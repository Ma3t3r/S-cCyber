import csv

def compare_csv(file1, file2):
    # carrega os dados dos arquivos CSV em dicionários
    with open(file1, 'r') as f1:
        reader1 = csv.DictReader(f1)
        data1 = [row for row in reader1]
    
    with open(file2, 'r') as f2:
        reader2 = csv.DictReader(f2)
        data2 = [row for row in reader2]

    # encontra as diferenças entre os dois arquivos CSV
    differences = []
    for row1 in data1:
        found = False
        for row2 in data2:
            if row1 == row2:
                found = True
                break
        if not found:
            differences.append(row1)
            
    # escreve as diferenças em um novo arquivo CSV
    with open('differences.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=reader1.fieldnames)
        writer.writeheader()
        for row in differences:
            writer.writerow(row)
    
    # gera um relatório com as diferenças
    report = f"Foram encontradas {len(differences)} diferenças entre os arquivos {file1} e {file2}."
    print(report)

file1 = 'file1.csv'
file2 = 'file2.csv'
compare_csv(file1, file2)
