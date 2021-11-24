# oracle 연결
import cx_Oracle

connection = cx_Oracle.connect('SCOTT/TIGER@XE')
cursor = connection.cursor()
querystring = "SELECT * FROM DEPT"
cursor.execute(querystring)

print(cursor.fetchall())

cursor.close()
connection.close()
'''
[(10, 'ACCOUNTING', 'NEW YORK'), (20, 'RESEARCH', 'DALLAS'), (30, 'SALES', 'CHICAGO'), (40, 'OPERATIONS', 'BOSTON')]
'''