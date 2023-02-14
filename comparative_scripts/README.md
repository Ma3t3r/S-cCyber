CSV Comparison and Report Generator
This script compares two CSV files and generates a report of the differences found between them.

Requirements
Python 3.x
The csv library
Usage
Place the two CSV files you want to compare in the same directory as the script.
Update the file1 and file2 variables with the names of your CSV files.
Run the script using the command python script.py.
Output
The script will output a report detailing the number of differences found between the two CSV files. It will also create a new CSV file named differences.csv that contains the rows that are different between the two original CSV files.

Note
The script assumes that both CSV files have the same number of columns and that the columns are in the same order. If the columns are not in the same order, the script will need to be modified to perform the correct comparison.