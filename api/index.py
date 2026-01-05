import pickle
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('web.html')
@app.route('/info',methods=['GET','POST'])
def appconnect():
    if(request.method=='POST'):
        geograph=int(request.form['geo'])
        gender=int(request.form['g'])
        age=int(request.form['age'])
        balance=int(request.form['bal'])
        noofprod=int(request.form['nop'])
        hascredit=int(request.form['has'])
        isactive=int(request.form['isa'])
        file=open('model.pkl','rb')
        model=pickle.load(file)
        result=model.predict([[geograph,gender,age,balance,noofprod,hascredit,isactive]])
        if(result==0):
            return render_template('web.html',answer='cutomer will stay')
        else:
            return render_template('web.html',answer='customer will churn')

