from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play',methods=['POST'])
def play():
    user_choice=request.form['choice']
    computer_choice=random.choice(['Rock','Paper','Scissors'])
    res=get_result(user_choice, computer_choice)
    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=res)

def get_result(user_choice, computer_choice):
    if user_choice==computer_choice:
        return "It's a tie!"
    elif(user_choice == 'Rock' and computer_choice=='Scissors') or (user_choice=='Paper' and computer_choice=='Rock') or (user_choice=='Scissors' and computer_choice=='Paper'):
        return "You win!"
    else:
        return "You lose!"
    
if __name__ =='__main__':
    app.run(debug=True)
         
    