
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from data_store import store_data
from flask_mysqldb import MySQL


import yaml
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)



app = Flask(__name__)

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_database']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/', methods =['POST','GET'])
def index():
    
         return render_template('index.html')

global lst
lst = dict()

global mylist
mylist = dict()

@app.route('/fatca', methods =['POST','GET'])
def fatca():
	if request.method == 'POST':
		pannumber = request.form.get('pannumber')
		from pan_number import pannumber_exist
		status = pannumber_exist(pannumber)
		redirected = False
		mylist['redirected'] = redirected
		if  status:
			redirected = True
			mylist['redirected'] = redirected
			
			
			
			from fetch_data import get_data

			returned_data = get_data(pannumber)
			global lst
			lst = returned_data.copy()

			return redirect(url_for('investment'),code=307)
		else:
			firstname = request.form.get('firstname')
			lastname = request.form.get('lastname')
			
			lst['pannumber']=pannumber
			mobilenumber = request.form.get('mobilenumber')
			lst['mobilenumber']=mobilenumber
			dateofbirth = request.form.get('dob')
			lst['dateofbirth']=dateofbirth
			emailid = request.form.get('emailid')
			lst['emailid']=emailid
			name = firstname + ' ' + lastname
			lst['name']=name
			print(lst['name'])
		
			return render_template('fatca.html', lst=lst)
	

@app.route('/nominee', methods =['POST','GET'])
def nominee():
	if request.method == 'POST':
		countryofbirth =request.form.get('birthcountry')
		lst['birthcountry'] = countryofbirth
		occupation = request.form.get('occupation')
		lst['occupation'] = occupation
		incomeslab = request.form.get('incomeslab')
		lst['incomeslab'] = incomeslab
		exposed_politically = request.form.get('politically_exposed')
		lst['politically_exposed'] = exposed_politically
		taxresident = request.form.get('taxresident')
		lst['taxresident'] = taxresident


		return render_template('nominee.html', lst=lst)
	else:
		return render_template('nominee.html', lst=lst)


@app.route('/investment', methods =['POST','GET'])
def investment():
	if request.method =='POST':
		
		if mylist['redirected']:
			return render_template('investment.html', lst=lst)
		else:
			title = request.form.get('title')
			nameofnominee = request.form.get('nameofnominee')
			lst['nomineename'] = title + ' ' + nameofnominee
			dob_nominee = request.form.get('dob_nominee')
			lst['dob_nominee'] = dob_nominee
			relationship = request.form.get('relationship')
			lst['relationship'] = relationship
			allocation = request.form.get('allocation')
			lst['allocation'] = allocation
			nomineenumber = request.form.get('nomineenumber')
			lst['nomineenumber'] = nomineenumber
			return render_template('investment.html', lst=lst)

@app.route('/bankdetails', methods = ['POST','GET'])
def bankdetails():
	if request.method == 'POST':
		investmenttype = request.form.get('investmenttype')
		lst['investmenttype'] = investmenttype
		category = request.form.get('category')
		lst['category'] = category
		schemename = request.form.get('schemename')
		lst['schemename'] =schemename
		option = request.form.get('option')
		lst['option'] = option
		amount = request.form.get('amount')
		lst['amount'] = amount
		arn = request.form.get('arn')
		lst['arn'] = arn
		euin = request.form.get('euin')
		lst['euin'] = euin

	return render_template('bankdetails.html', lst=lst)

@app.route('/review', methods = ['POST','GET'])
def review():
	if request.method == 'POST':
		bankname = request.form.get('bankname')
		lst['bankname'] = bankname
		accounttype = request.form.get('accounttype')
		lst['accounttype'] = accounttype
		accountnumber = request.form.get('accountnumber')
		lst['accountnumber'] = accountnumber
		ifsc = request.form.get('ifsc')
		lst['ifsc'] = ifsc
		paymentmode = request.form.get('modeofpayment')
		lst['paymentmode'] = paymentmode
		print(lst)



	return render_template('review.html', lst=lst)

@app.route('/thankyou', methods = ['POST','GET'])
def thankyou():	
	if request.method == 'POST':
		from data_store import store_data
		print(lst)

		store_data(lst,db,mysql)

	return render_template('thankyou.html', lst=lst)


if __name__ == '__main__':
    app.run(debug = True)
