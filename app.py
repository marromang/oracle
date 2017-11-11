import cx_Oracle
from bottle import Bottle,route,run,request,template,static_file

@route('/')
def inicio():
	return template ('form.tpl')

@route('/apuestas',method='POST')
def apuestas():
	carrera = request.forms.get("carrera")
	con = cx_Oracle.connect("C##prac2user/prac2user@//87.221.173.197:1521/ORCL")
	curs = con.cursor()
	curs.execute("select c.dni, c.nombre||' '||c.apellido1||' '||c.apellido2, a.codigoCaballo, a.importeApostado from apuestas a, clientes c where c.dni = a.dniCliente and codigoCarrera = %s"carrera)
	datos= []
	for c in curs:
		datos.append(c)

	return template('consulta.tpl', datos=datos)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='0.0.0.0', port= 8080)
