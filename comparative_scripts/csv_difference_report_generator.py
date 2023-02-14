import csv
import openpyxl
import os

def xlsx_to_csv(file):
    # load the .xlsx file as a workbook
    workbook = openpyxl.load_workbook(file)

    # for each sheet, save as a separate .csv file
    for sheet in workbook:
        sheet_name = sheet.title
        csv_file = f"{sheet_name}.csv"

        with open(csv_file, 'w', newline='') as f:
            csv_writer = csv.writer(f)

            for row in sheet.iter_rows():
                row_values = [cell.value for cell in row]
                csv_writer.writerow(row_values)

        # return the name of the converted .csv file
        return csv_file

def compare_csv(file1, file2):
    # check if either file is .xlsx and convert it to .csv if so
    if file1.endswith('.xlsx'):
        file1 = xlsx_to_csv(file1)
    if file2.endswith('.xlsx'):
        file2 = xlsx_to_csv(file2)

    # load the data from the CSV files into dictionaries
    with open(file1, 'r') as f1:
        reader1 = csv.DictReader(f1)
        data1 = [row for row in reader1]
    
    with open(file2, 'r') as f2:
        reader2 = csv.DictReader(f2)
        data2 = [row for row in reader2]

    # find the differences between the two CSV files
    differences = []
    for row1 in data1:
        found = False
        for row2 in data2:
            if row1 == row2:
                found = True
                break
        if not found:
            differences.append(row1)
            
    # write the differences to a new CSV file
    with open('differences.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=reader1.fieldnames)
        writer.writeheader()
        for row in differences:
            writer.writerow(row)
    
    # generate a report with the differences
    report = f"Found {len(differences)} differences between the files {file1} and {file2}."
    print(report)
    
    # count the number of values in the "IP Address" column of both files
    count1 = sum(1 for row in data1 if row.get("IP Address"))
    count2 = sum(1 for row in data2 if row.get("IP Address"))
    print(f"File {file1} has {count1} values in the 'IP Address' column.")
    print(f"File {file2} has {count2} values in the 'IP Address' column.")
    
    # create the "All Hosts.csv" file
    with open('All Hosts.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=reader1.fieldnames)
        writer.writeheader()

        # write all the rows from both files to the "All Hosts.csv" file
        for row in data1 + data2:
            writer.writerow(row)

# prompt the user to enter the names of the two files to compare
file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")

# compare the two files and create the "All Hosts.csv" file
compare_csv(file1, file2)

