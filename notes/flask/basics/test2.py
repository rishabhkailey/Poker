from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('test2.html',list = [10,20])
if __name__ == '__main__':
	print(app.config)
	app.config['DEBUg'] = True
	app.run()