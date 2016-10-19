from flask import Flask, flash, redirect, render_template, url_for

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/')
def index():
  return render_template('index.html')
  
  return "Root Page"

@app.route('/login/<message>/') 
def login(message):
  if(message != None):
    flash(message)
  flash("A default message")
  return "Let's pretend you just loggen in"

if __name__ == "__main__": 
  app.run(host='0.0.0.0', debug=True)
