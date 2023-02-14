def compare_csv(file1, file2):
    # read the data from the first file
    with open(file1, 'r') as f:
        reader1 = csv.DictReader(f)
        data1 = [row for row in reader1]

    # read the data from the second file
    with open(file2, 'r') as f:
        reader2 = csv.DictReader(f)
        data2 = [row for row in reader2]

    # find the differences between the two files
    differences = []
    for row1 in data1:
        found = False
        for row2 in data2:
            if row1 == row2:
                found = True
                break
        if not found:
            differences.append(row1)

    # write the differences to a new file "differences.csv"
    with open("differences.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=reader1.fieldnames)
        writer.writeheader()
        for row in differences:
            writer.writerow(row)

    # print the number of differences found
    print(f"Found {len(differences)} differences between the files {file1} and {file2}.")

# prompt the user to enter the names of the two files to compare
file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")

# compare the two files and create the "differences.csv" file
compare_csv(file1, file2)
