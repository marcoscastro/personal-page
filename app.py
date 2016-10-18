from bottle import route, run
from bottle import static_file, request
from bottle import template, get, error
import os

# static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

@route('/')
def index():
	return template('index')

@route('/skills')
def skills():
	return template('skills')

@route('/about')
def about():
	return template('about')

@route('/courses')
def courses():
	return template('courses')

@route('/contact', method='POST')
def acao_login():
	name = request.forms.get('name')
	email = request.forms.get('email')
	site = request.forms.get('site')
	message = request.forms.get('message')
	print(message)
	return template('contact', name=name)

@error(404)
def error404(error):
	return template('oops')

if __name__ == "__main__":
	if os.environ.get('APP_LOCATION') == 'heroku':
		run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
	else:
		print('ENTROU AQUI')
		run(host='localhost', port=8080, debug=True, reloader=True)