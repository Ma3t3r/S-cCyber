import csv
import openpyxl
import os

i = 0

def xlsx_to_csv(file):
    global i

    # carrega o arquivo .xlsx como workbook
    workbook = openpyxl.load_workbook(file)

    # para cada planilha, salva como um arquivo .csv separado
    for sheet in workbook:
        i += 1
        sheet_name = sheet.title + str(i)
        csv_file = f"{sheet_name}.csv"

        with open(csv_file, 'w', newline='') as f:
            csv_writer = csv.writer(f)

            for row in sheet.iter_rows():
                row_values = [cell.value for cell in row]
                csv_writer.writerow(row_values)

        # retorna o nome do arquivo .csv convertido
        print(csv_file)
        return csv_file

def compare_csv(file1, file2):
    # verifica se algum dos arquivos é .xlsx e, se for, o converte para .csv
    if file1.endswith('.xlsx'):
        file1 = xlsx_to_csv(file1)
    if file2.endswith('.xlsx'):
        file2 = xlsx_to_csv(file2)

    # lê os dados do primeiro arquivo
    with open(file1, 'r') as f:
        reader1 = csv.DictReader(f)
        data1 = [row for row in reader1]

    # lê os dados do segundo arquivo
    with open(file2, 'r') as f:
        reader2 = csv.DictReader(f)
        data2 = [row for row in reader2]

    # encontra as diferenças entre os dois arquivos
    differences = []
    for row1 in data1:
        found = False
        for row2 in data2:
            if row1 == row2:
                found = True
                break
        if not found:
            differences.append(row1)

    # adiciona marcação nos campos diferentes e contagem na coluna Hostname
    count_diff = 0
    for row in differences:
        row_str1 = str([val for val in row.values()])
        for row2 in data2:
            row_str2 = str([val for val in row2.values()])
            if row_str1 == row_str2:
                for key, val in row.items():
                    if row2[key] != val:
                        row[key] = f"***{val}***"
                if row2['Hostname'] != row['Hostname']:
                    row['Hostname'] = f"***{row['Hostname']} ({row2['Hostname']})***"
                count_diff += 1

    # escreve as diferenças em um novo arquivo "differences.csv"
    with open("differences.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=reader1.fieldnames)
        writer.writeheader()
        for row in differences:
            writer.writerow(row)

    # imprime o número de diferenças encontradas
    print(f"Found {count_diff} differences between the files {file1} and {file2}.")

    # conta o número de valores na coluna "Hostname" de ambos os arquivos
    count1 = sum(1 for row in data1 if row.get("Hostname"))
    count2 = sum(1 for row in data2 if row.get("Hostname"))
    print(f"File {file1} has {count1} values in the 'Hostname' column.")
    print(f"File {file2} has {count2} values in the 'Hostname' column.")

    # print the number of differences found
    print(f"Found {len(differences)} differences between the files {file1} and {file2}.")
    
     # count the number of values in the "IP Address" column of both files
    count1 = sum(1 for row in data1 if row.get("IP Address"))
    count2 = sum(1 for row in data2 if row.get("IP Address"))
    print(f"File {file1} has {count1} values in the 'IP Address' column.")
    print(f"File {file2} has {count2} values in the 'IP Address' column.")

# prompt the user to enter the names of the two files to compare
file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")

# compare the two files and create the "differences.csv" file
compare_csv(file1, file2)
