from bottle import route, run, template, get, static_file

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

if __name__ == "__main__":
	run(host='localhost', port=8080, reloader=True, debug=True)