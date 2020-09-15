from flask import Flask,session,render_template,request,jsonify, redirect,url_for
from numpy.core import unicode

import main

#importing package to connect flask to mysql database
from flaskext.mysql import MySQL


nlpsql = Flask(__name__)
mysql = MySQL()
nlpsql.config['MYSQL_DATABASE_USER'] = 'root'
nlpsql.config['MYSQL_DATABASE_PASSWORD'] = ''
nlpsql.config['MYSQL_DATABASE_DB'] = 'nlp'
nlpsql.config['MYSQL_DATABASE_HOST'] = 'localhost'
nlpsql.config['MYSQL_DATABASE_PORTNUMBER'] = 3306
mysql.init_app(nlpsql)

#getting mysql result for the input query
def getQuery():
	query=request.form['query']
	print(query)
	#processQuery converts the input query to mysql query
	query = main.processQuery(query)

	#execute mysql query
	cursor = mysql.connect().cursor()
	cursor.execute(query)
	data = cursor.fetchall()
	
	#converting from unicode to UTF-8
	encodedData = []
	for row in data:
		encodedrow = []
		for item in row:
			if(isinstance(item,unicode)):
				encodedrow.append(item.encode("utf-8"))
			else:
				encodedrow.append(item)
		encodedData.append(encodedrow)
			
	
	#creating html table for  Query result
	htmlResult="<span class='terminal-text-precommand'>user@snlp-sql</span><span class='terminal-text-command'>:~$ : <span 		class='terminal-text-command'>"+query+"</span><hr /><table class='table-bordered display-table'>"
		
	for tableRow in encodedData:
		htmlResult=htmlResult+"<tr>"
		for tablecell in tableRow:
			htmlResult=htmlResult+"<td>"+str(tablecell)+"</td>"
		htmlResult=htmlResult+"</tr>"
	htmlResult=htmlResult+"</table>"
	
	#converts html to jason format
	return jsonify(htmlResult)


#to get Student database similar to getQuery
@nlpsql.route('/showStudentDetails',methods=['POST'])
def showStudentDetails():
	query="select * from student"
	query = main.processQuery(query)
	cursor = mysql.connect().cursor()
	cursor.execute(query)
	data = cursor.fetchall()
	encodedData = []
	for row in data:
		encodedrow = []
		for item in row:
			if(isinstance(item,unicode)):
				encodedrow.append(item.encode("utf-8"))
			else:
				encodedrow.append(item)
		encodedData.append(encodedrow)
				
	studentTable="";
	for row in encodedData:
		studentTable=studentTable+"<tr>"
		for cell in row:
			studentTable=studentTable+"<td>"+str(cell)+"</td>"
		studentTable=studentTable+"</tr>"

	studentTable=studentTable+""

	print(studentTable)
	return jsonify(studentTable)

#to get department database similar to getQuery
@nlpsql.route('/showDepartmentDetails',methods=['POST'])
def showDepartmentDetails():
	query="select * from department"
	query = main.processQuery(query)
	cursor = mysql.connect().cursor()
	cursor.execute(query)
	data = cursor.fetchall()
	encodedData = []
	for row in data:
		encodedrow = []
		for item in row:
			if(isinstance(item,unicode)):
				encodedrow.append(item.encode("utf-8"))
			else:
				encodedrow.append(item)
		encodedData.append(encodedrow)
				
	departmentTable="";
	for row in encodedData:
		departmentTable=departmentTable+"<tr>"
		for cell in row:
			departmentTable=departmentTable+"<td>"+str(cell)+"</td>"
		departmentTable=departmentTable+"</tr>"


	print(departmentTable)
	return jsonify(departmentTable)

#main function which runs the flask app
if __name__ == '__main__':
	nlpsql.run()
