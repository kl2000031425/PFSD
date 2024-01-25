import mysql

conn=mysql.connect('PFSD')
print('Database created')

#conn.execute('''CREATE TABLE sqltable (ID number,name text,mark number)''')
print('table created')

conn.execute("Insert into sqltable values(2000031425,'Joseph',20)")
print('data inserted')

#cur=conn.cursor()

#data1={(3456,"jack",32),(5463,"rahul",43)}
#cur.executemany('INSERT INTO sqltable VALUES(?,?,?);',data1);
#print('inserted multiple data')
#cur.execute("UPDATE sqltable SET name='john' where name='rahul'")
#print('updated successfully')
#cur.execute("DELETE from sqltable where ID='5463")
#print('row deleted')

conn.commit()
conn.close()