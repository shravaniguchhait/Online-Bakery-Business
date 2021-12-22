from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
     return render_template('homepage.html')

@app.route('/aboutus/')   
def aboutus():
     return render_template('aboutus.html')

@app.route('/orderonline/')    
def orderonline():
     return render_template('orderonline.html')

@app.route('/CakesandCupcakes/')   
def CakesandCupcakes():
     return render_template('CakesandCupcakes.html')

@app.route('/DoughnutsandBeverages/')   
def DoughnutsandBeverages():
     return render_template('DoughnutsandBeverages.html')

@app.route('/contactUs/')   
def contactUs():
     return render_template('contactUs.html')

@app.route('/Email Now/')   
def EmailNow():
     return render_template('EmailNow.html')

@app.route('/placeorder/')   
def placeorder():
     return render_template('placeorder.html')

if __name__=='__main__':
    app.run(debug=True)

