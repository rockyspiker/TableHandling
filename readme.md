# Table Handling
## Description
table.py creates many functions that can be called on a database to make changes.
main.py is just example calls to the tables and functions.
## table.py
### __init__
Initializes the Table class.
### __str__
Formats the print of the class.
### select(self,field,val)
Using field to find the index, select finds all rows that contain the give val in the given field.
### project(self, *fields)
Given x amount of fields, project will print off all rows, but only the columns of the given fields.
### join(tab1, tab2)
Joins the two tables together on their shared field, which is discovered in this function as well.
### insert(self, *tup)
Inserts a row with the given values in tup, as long as the length of *tup is the same as the amount of fields.
### remove(self, field, val)
Removes all rows that contain the given val in the given field.
### store(self)
Stores the table using pickle
### restore(fname)
Restores the table from fname using pickle
### read(fname)
Creates a table based on the values from fname
### write(self,fname)
Writes to (creates if needed) fname a table in the same format as it would be read.
