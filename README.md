## Project title
Objective of the project is to create a streamline to upload the data about material properties to a Sqlite3 database

## Tech/framework used
Python3.6

## Code Example

## Installation
pip install -r requirements.txt

## Tests

## How to use?
The main.py file has options of what type of operations to be performend on the database. So, we can change the input conditions as needed and input the required data file locations and run it.
The list of operations that can be performed currently are:
1) "data_insertion"

To run: python main.py "data_insertion" "../materials_parameters_noUnits_noColumnHeadings.csv"

## To be done
1) Code cleaning and streamlining to be done in seperating the SQL codes from the .py files

To include more operations on the database like:
2) "data_deletion"
3) "column_addition"
4) "column_deletion"

