from flask import Flask, render_template,request
app=Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('car_pur.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/predictt',methods =['POST'])

def predictt():
    p=request.form["Gender"]
    if(p=="male"):
        p=0
    elif(p=="female"):
        p=1
    q=request.form["Age"]
    r=request.form["EstimatedSalary"]
    t = [[float(p),float(q),float(r)]]
    output = model.predict(t)
    
    
    if output==0:
        prediction="No,the person is not going to make a car purchase."
    elif output==1:
        prediction="Yes,the person will make a car purchase"

    return render_template("after.html",y=prediction)

if __name__ == '__main__' :
    app.run(debug=True)