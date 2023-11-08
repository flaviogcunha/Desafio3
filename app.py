from flask import Flask, render_template
app = Flask(__name__) 
@app.route('/')
def home():
    return render_template ('home.html')
@app.route('/marcantes')
def marcantes():
    return render_template ('marcantes.html')
@app.route('/titulos')
def titulos():    
    return render_template ('titulos.html')