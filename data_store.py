import yaml
from flask import Flask





def store_data(lst,db,mysql):

   
    name = lst['name']
    pannumber = lst['pannumber']
    mobilenumber = lst['mobilenumber']
    dateofbirth = lst['dateofbirth']
    emailid = lst['emailid']
	

    countryofbirth = lst['birthcountry']
    occupation = lst['occupation']
    incomeslab = lst['incomeslab']
    politically_exposed = lst['politically_exposed']
    taxresident = lst['taxresident']

    nomineename = lst['nomineename']
    dob_nominee = lst['dob_nominee']
    relationship = lst['relationship']
    allocation = lst['allocation']
    nomineenumber = lst['nomineenumber']

    investmenttype = lst['investmenttype']
    category = lst['category']
    schemename = lst['schemename']
    option = lst['option']
    amount = lst['amount']
    arn = lst['arn']
    euin = lst['euin']

    bankname =  lst['bankname']
    accounttype = lst['accounttype']
    accountnumber = lst['accountnumber']
    ifsc = lst['ifsc']
    paymentmode = lst['paymentmode']


    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO purchase_prac1(First_Applicant,\
    Pan_Number,\
    Email_ID,\
    Phone_Number,\
    DOB_F_Applicant,\
    Birth_Country,\
    Occupation,\
    Income_Slab,\
    Politically_Exposed,\
    Tax_Resident,\
    Nominee_Name,\
    DOB_Nominee,\
    Relationship,\
    Allocation,\
    Nominee_Number,\
    Investment_Type,\
    Category,\
    Scheme_Name,\
    Scheme_Option,\
    Amount,\
    ARN,\
    EUIN,\
    Bank_Name,\
    Account_Type,\
    Account_Number,\
    IFSC_Code,\
    Payment_Mode) \
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (name,pannumber,emailid,mobilenumber,dateofbirth,
    countryofbirth,occupation,incomeslab,politically_exposed,taxresident,
    nomineename,dob_nominee,relationship,allocation,nomineenumber,
    investmenttype,category,schemename,option,amount,arn,euin,
    bankname,accounttype,accountnumber,ifsc,paymentmode)
    )
    mysql.connection.commit()