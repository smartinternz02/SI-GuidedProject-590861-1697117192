from flask import Flask, render_template,request
app=Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('car_purchase.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/predict',methods =['POST'])

def predict():
    p=request.form["Gender"]
    if(p=="male"):
        p=0
    elif(p=="female"):
        p=1
    q=request.form["Age"]
    r=request.form["EstimatedSalary"]
    t = [[float(p),float(q),float(r)]]
    output = model.predict(t)
    print(output)
    
    if output==0:
        prediction="No, the person will not make a purchase"
    else:
        prediction="Yes, The person will make a purchase"

    return render_template("index.html",prediction)

if __name__ == '__main__' :
    app.run(debug=True)