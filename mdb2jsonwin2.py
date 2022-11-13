import json, pyodbc

#Input data
MDB =  input('Type path to the mdb file: ')
JSON = input('Type path to the json file: ')

#Reading the mdb file
# set up some constants
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}';PWD = 'pw'

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()

print(' ')
print('Table list:')
print(' ')

# declaring the table list
tables=[]

# display tables in the database
for i in cur.tables(tableType='TABLE'):
    print(i.table_name)
    tables.append(i.table_name)

print(' ')

# select the table
table = input('Select the table: ')

# list of the values selected from the table
selected = table.split(", ")

#The output dictionary
d={}

# finding the selected tables in the list and transfering the found to json
for i in tables:
    for j in selected:
        if((j==i)or(table=='*')):
            # run a query and get the results
            
            SQL = 'SELECT * FROM {};'.format(i)# your query goes here
            rows = cur.execute(SQL).fetchall()
                        
            #Converting the elements of the rows list from tuple to list
            for k in range(len(rows)):
                rows[k]=list(rows[k])
            
            #Writing into the output dictionary
            d.update({i:rows})            
            
            del SQL, rows

cur.close()
con.close()

#Writing into json file
with open(JSON,"a") as jf:
    json.dump(d, jf, ensure_ascii=False)

print(' ')
print('All data has been written successfully')