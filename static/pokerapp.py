from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
	return render_template('home.html')


@app.route('/rishabh')
def welcome2():
	return "hello2"

if __name__ == '__main__':
	print(app.config)
	app.config['DEBUG'] = True
	app.run()