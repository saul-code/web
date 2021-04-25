from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

#metodo con parametros
@app.route('/user/')
@app.route('/user/<name>')
def user(name = 'Saul'):
	my_list= [1,2,3,4]
	age = 18
	return render_template('pyenhtml.html', nombre=name, lista= my_list, edad = age)


if __name__ == '__main__':
	app.run(debug=True)