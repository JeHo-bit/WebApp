from flask import Flask

app= Flask(__name__)

my_cart = {1: 'orange', 2: 'maxi skirt', 3: 'hermes slippers', 4: 'vegetables'}

@app.route('/')
def index():
    return 'Hello World'

@app.route('/items')
def getAllItems():
    return my_cart

@app.route('/items/first')
def getFirstItems():
    return my_cart[1]

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    
