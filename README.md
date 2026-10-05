# Employee Directory Program

This project implements a simple employee directory application in Python using classes, file I/O, and dictionaries.

## Overview

The program manages employee records with the following attributes:
- ID
- Name
- Department
- Pay

It reads employee data from a text file, updates an in-memory list of Employee objects, adds/removes employees, converts the data to a dictionary, and prints the dictionary in the required format.

## Files

- `employee_directory_neupane_salin.py` — main Python program
- `employees.txt` — initial employee data file
- `instruction.pdf` — assignment instructions

## How to Run

From the terminal, run:

```bash
python3 "/Users/lincoln/Desktop/Python/employee_directory_neupane_salin.py"
```

## Program Behavior

The program:
1. Loads employee records from `employees.txt`
2. Creates employee objects using the `Employee` class
3. Adds two employees: `Emp1` and `Emp2`
4. Tries to delete `Emp3`, which is intentionally not present, to match the sample output
5. Converts the employee list into a dictionary keyed by:
   - `ID`
   - `name`
   - `department`
   - `pay`
6. Prints the employee dictionary in a clean, readable format

## Sample Output

```text
ID:108 does not exist, deletion is aborted
ID        : [101, 102, 103, 104, 105, 106, 107]
name      : ['JSmith', 'MJones', 'CBrown', 'TCook', 'JWhite', 'Emp1', 'Emp2']
department: ['Accounting', 'Sales', 'HR', 'IT', 'Sales', 'Accounting', 'Sales']
pay       : [75000.0, 60000.0, 55000.0, 95000.0, 70000.0, 56000.0, 80000.0]
```

## Author

Salin Neupane
