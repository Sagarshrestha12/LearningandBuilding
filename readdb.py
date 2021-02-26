import sqlite3
import csv
def insert_db(filename1):
    conn=sqlite3.connect('result.db')
    c=conn.cursor()
    c.execute('''DROP TABLE result''')
    c.execute('''CREATE TABLE result 
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    MATH REAL);''')
    with open(filename1,newline='') as csvfile:
        data=csv.DictReader(csvfile)
        for row in data:
            c.execute('''INSERT INTO result 
                (ID,NAME,MATH) VALUES 
                    (?,?,?)''',(row['ID'],row['NAME']
                        ,row['MATH'],))
            conn.commit()
        conn.close()
def update_db(ID,MATH1):
    conn=sqlite3.connect('result.db')
    c=conn.cursor()
    c.execute('''UPDATE result
    SET MATH= ? WHERE ID=?''',(MATH1,ID,))
    conn.commit()
    conn.close()
def fetch(ID1):
    conn=sqlite3.connect('result.db')
    c=conn.cursor()
    c.execute('''SELECT * FROM result WHERE ID=?''',(ID1,))
    x=c.fetchall()
    return x[0]
