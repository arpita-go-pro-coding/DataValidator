import cx_Oracle
"""
user,pswd,host,port,sid='hr', 'hr', 'localhost', '1521', 'ORCL'
conn_str=f"{ user}/{ pswd}@//{ host}:{ port}/{sid}"
connection_done = conn_str.cursor()

sql_select="""
#select * from HR.LOCATIONS where country_id in('CA','UK','DE')
"""
connection_done.execute(sql_select)
for row in connection_done:
            # print( row[0], "-", row[1])
    print(row)
"""

db_hr = cx_Oracle.connect('hr', 'hr', 'localhost:1521/ORCL')
cursor = db_hr.cursor()
cursor.execute("SELECT * FROM HR.LOCATIONS where country_id in('CA','UK','DE')")
for row in cursor:
    print(row)

db_scott = cx_Oracle.connect('scott', 'scott', 'localhost:1521/ORCL')
cursor = db_scott.cursor()
cursor.execute("SELECT * FROM SCOTT.LOCATIONS_STG where country_id in('CA','UK','DE')")
for row in cursor:
    print(row)