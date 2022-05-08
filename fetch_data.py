
def get_data(pannumber):
	lst = dict()
	import yaml
	db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
	import mysql.connector as sql
	connection = sql.connect(
			host= db['mysql_host'],
			user= db['mysql_user'],
			password= db['mysql_password'],
			database= db['mysql_database'],
			auth_plugin='mysql_native_password'
		)
	cursor = connection.cursor()

	command = "Select ID, First_Applicant,Pan_Number,Email_ID,Phone_Number, DOB_F_Applicant, \
	            Birth_Country,Occupation,Income_Slab,Politically_Exposed,Tax_Resident, \
	            Nominee_Name,DOB_Nominee,Relationship, Allocation,Nominee_Number \
	            from purchase_prac1 WHERE Pan_Number= %s "
	values = (pannumber,)
	cursor.execute(command,values)
	colmns = cursor.fetchall()
	data = colmns[0]


	lst['name'] = data[1]
	lst['pannumber'] = data[2]
	lst['mobilenumber'] = data[4]
	lst['dateofbirth'] = data[5]
	lst['emailid'] = data[3]


	lst['birthcountry'] = data[6]
	lst['occupation'] = data[7]
	lst['incomeslab'] = data[8]
	lst['politically_exposed'] = data[9]
	lst['taxresident'] = data[10]

	lst['nomineename'] = data[11]
	lst['dob_nominee'] = data[12]
	lst['relationship'] = data[13]
	lst['allocation'] = data[14]
	lst['nomineenumber'] = data[15]

	return lst
