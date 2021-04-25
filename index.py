from flask import Flask, render_template, request

#agrego una carpeta template
app = Flask(__name__, template_folder = "templates")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

#metodo con parametros
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>/')
def params(name = '', num = ''):
	#param = request.args.get('params1','no hay parametro')
	#param_2 = request.args.get('params2', 'no hay parametro')
	return 'regreso: {}, {}'.format(name,num)


if __name__ == '__main__':
	app.run(debug=True)