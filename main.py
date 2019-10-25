#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
from IPython import embed
import pandas as pd
import numpy as np
from database_creation import create_connection
from table_creation import create_table
from rows_insertion import rows_insertion


def main(objective, data_input_path):

	dirpath = os.getcwd()
	database = os.path.join(dirpath, "pythonsqlite.db")

	# create a database connection
	conn = create_connection(database)

	# create tables
	if conn is not None:
	    # create projects table
	    create_table(conn)
	else:
	    print("Error! cannot create the database connection.")

	if objective == "data_insertion":
		tobe_input_data = pd.read_csv(data_input_path, header = None)
		last_row_id = rows_insertion(conn, tobe_input_data.values.tolist())
	elif objective == "data_deletion":
		pass
	else:
		pass

	return True

if __name__ == '__main__':
	# main("data_insertion", "/home/sahit/Documents/Material_Science_Project/materials_param_noUnits.csv")
	main(sys.argv[1], sys.argv[2])

