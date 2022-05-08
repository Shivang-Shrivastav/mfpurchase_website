

def pannumber_exist(pannumber):

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

		command = "Select Scheme_Name,Amount from purchase_prac1 WHERE Pan_Number= %s"
		values = (pannumber,)

		cursor.execute(command,values)
		lst = cursor.fetchall()
		if len(lst) > 0:
			return True
		else:
			return False