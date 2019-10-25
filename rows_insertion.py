# -*- coding: utf-8 -*-

from IPython import embed

def rows_insertion(conn, rows_list):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = """INSERT  OR IGNORE INTO material_properties (
                                    'Material' ,  
                                    'Literature Reference' ,  
                                    'Stoichiometric Formula (AxByCz)' , 
                                    'Element A Name' ,  
                                    'Element B Name' ,  
                                    'Element C Name' , 
                                    'Element D Name' ,  
                                    'Element E Name' ,  
                                    'Atomic ratio A' , 
                                    'Atomic ratio B' ,  
                                    'Atomic ratio C' ,  
                                    'Atomic ratio D' ,  
                                    'Atomic ratio E' , 
                                    'Atomic % A' ,  
                                    'Atomic % B' ,  
                                    'Atomic % C' ,  
                                    'Atomic % D' ,  
                                    'Atomic % E' , 
                                    'Element A Weight' , 
                                    'Element B Weight' , 
                                    'Element C Weight' , 
                                    'Element D Weight' , 
                                    'Element E Weight' , 
                                    'Element A Radii', 
                                    'Element B Radii', 
                                    'Element C Radii', 
                                    'Element E Radii', 
                                    'Element F Radii', 
                                    'Bond Energy', 
                                    'Bond Length', 
                                    'Bond Angle', 
                                    'Hull Energy', 
                                    'Amorphous structure', 
                                    'Crystallline structure', 
                                    'Metastable structure', 
                                    'PVD method' , 
                                    'Target A' , 
                                    'Target B' , 
                                    'Target C' , 
                                    'Target D' , 
                                    'Base Pressure' , 
                                    'Deposition Pressure' , 
                                    'Deposition Rate' , 
                                    'Argon flow rate' , 
                                    'Nitrogen flow rate' , 
                                    'Oxied flow rate' , 
                                    'Hydrogen flow rate' , 
                                    'Power of Target A' , 
                                    'Power of Target B' , 
                                    'Power of Target C' , 
                                    'Power of Target D' , 
                                    'Starting Substrate' , 
                                    'Substrate Temperature' , 
                                    'Film Thickness'
                                ) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    for row in rows_list:
        cur.execute(sql, row)
    conn.commit()
    return cur.lastrowid