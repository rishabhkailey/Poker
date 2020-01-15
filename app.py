from flask import Flask,render_template,request
import random

import jinja2
env = jinja2.Environment()
env.globals.update(zip=zip)

app=Flask(__name__)

@app.route('/')
def welcome():
	return render_template('welcome.html')

@app.route('/start')
def start():

	your_cards = get_cards(2)
	extra_cards = get_cards(5)
	opponent_cards = get_cards(5)
	hidden_cards = ['cover']*5
	return render_template('start.html',hand1 = your_cards,hand2 = opponent_cards,extra = hidden_cards,real_extra = extra_cards,index = str(1),bet = '0')

@app.route('/check',methods = ['POST'])
def check():
	import ast
	your_cards = ast.literal_eval(request.form.get("your"))
	opponent_cards = ast.literal_eval(request.form.get("opponent"))
	hidden_cards = ast.literal_eval(request.form.get("extra"))
	extra_cards = ast.literal_eval(request.form.get("real_extra"))
	index =  int(request.form.get("card_number"))
	bet1 =  int(request.form.get("bet"))
	hidden_cards[index-1] = extra_cards[index-1]
	return render_template('start.html',hand1 = your_cards,hand2 = opponent_cards,extra = hidden_cards,real_extra = extra_cards,index = str(index+1),bet = str(bet1))





@app.route('/deal',methods=['POST'])
def deal():
	import ast
	your_cards = ast.literal_eval(request.form.get("your"))
	opponent_cards = ast.literal_eval(request.form.get("opponent"))
	selected_cards = str(request.form.get("selected"))

	for i in range(0,6,2):
		your_cards.append(selected_cards[i]+selected_cards[i+1])
	return render_template('deal.html',hand1 = your_cards,hand2 = opponent_cards)








'''@app.route('change_cards')
def change():
	return render_template('start.html',hand1 = get_cards(),hand2 = get_cards())'''



def get_cards(x):
	ranks = '23456789TJKA'
	suits = '0123'
	
	cards=[]
	for i in ranks:
		for j in suits:
			cards.append(i+j)


	hand = []
	for i in range(x):
		hand.append(random.choice(cards))
	
	random.shuffle(hand)
	#print(cards)
	return hand


if __name__ == '__main__':
	print(app.config)
	app.config['DEBUG'] = True
	app.run()