from mdb_parser import MDBParser, MDBTable
import json

#Path to mdb file
pmdb=input('Type path to the mdb file: ')

#Path to json file
pjson=input('Type path to the json file: ')

#DB-Variable
db=MDBParser(pmdb)

print(db.tables)

table=input('select tables: ')

#list of the values selected from the table
selected = table.split(", ")

#finding the selected tables in the list and transfering the found to json
for i in db.tables:
	for j in selected:
		if((j==i)or(table=='*')):
		
			# Get a table from the DB.
			gtable = db.get_table(i)

			#Convert it to a dictionary
			dtable=dict(gtable)

			#Write a dictionary to json
			with open(pjson, "a") as jf:
				json.dump(dtable, jf)

print(' ')
print('All data written successfully')
