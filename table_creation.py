# -*- coding: utf-8 -*-

import os
from sqlite3 import Error

dirpath = os.getcwd()
print("current directory is : " + dirpath) 

# create_table_sql = open(os.path.join(dirpath, "columns_desc.txt"), "r")
# print(create_table_sql.read())

def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS material_properties (
                                    'Material' text   PRIMARY KEY, 
                                    'Literature Reference' text  , 
                                    'Stoichiometric Formula (AxByCz)' text  ,
                                    'Element A Name' text  , 
                                    'Element B Name' text  , 
                                    'Element C Name' text  ,
                                    'Element D Name' text  , 
                                    'Element E Name' text  , 
                                    'Atomic ratio A' integer  ,
                                    'Atomic ratio B' integer  , 
                                    'Atomic ratio C' integer  , 
                                    'Atomic ratio D' integer  , 
                                    'Atomic ratio E' integer  ,
                                    'Atomic % A' REAL  , 
                                    'Atomic % B' REAL  , 
                                    'Atomic % C' REAL  , 
                                    'Atomic % D' REAL  , 
                                    'Atomic % E' REAL  ,
                                    'Element A Weight' REAL  ,
                                    'Element B Weight' REAL  ,
                                    'Element C Weight' REAL  ,
                                    'Element D Weight' REAL  ,
                                    'Element E Weight' REAL  ,
                                    'Element A Radii' REAL ,
                                    'Element B Radii' REAL ,
                                    'Element C Radii' REAL ,
                                    'Element E Radii' REAL ,
                                    'Element F Radii' REAL ,
                                    'Bond Energy' text ,
                                    'Bond Length' text ,
                                    'Bond Angle' text ,
                                    'Hull Energy' text ,
                                    'Amorphous structure' text ,
                                    'Crystallline structure' text ,
                                    'Metastable structure' text ,
                                    'PVD method' text  ,
                                    'Target A' REAL  ,
                                    'Target B' REAL  ,
                                    'Target C' REAL  ,
                                    'Target D' REAL  ,
                                    'Base Pressure' REAL  ,
                                    'Deposition Pressure' REAL  ,
                                    'Deposition Rate' REAL  ,
                                    'Argon flow rate' REAL  ,
                                    'Nitrogen flow rate' REAL  ,
                                    'Oxied flow rate' REAL  ,
                                    'Hydrogen flow rate' REAL  ,
                                    'Power of Target A' REAL  ,
                                    'Power of Target B' REAL  ,
                                    'Power of Target C' REAL  ,
                                    'Power of Target D' REAL  ,
                                    'Starting Substrate' text  ,
                                    'Substrate Temperature' REAL  ,
                                    'Film Thickness' REAL  
                                );""")
    except Error as e:
        print(e)