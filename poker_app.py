from flask import Flask,render_template
# render_template helps to give path of html file in python file


app = Flask(__name__)

@app.route('/')
def welcome():
	return 'hello'
#    card1 = "20.png"
 #   return render_template('poker.html',show=card1)

@app.route('/jassi')
def method():
    return 'yoooo'

if __name__ == '__main__':
    print(app.config)
    app.config['DEBUG'] = True
    app.run()