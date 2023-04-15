from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
import joblib
model=pickle.load(open("placemenet123.pkl",'rb'))
ct=joblib.load('placement')
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/guest',methods =["POST"])
def Guest():
    send1=request.form["send1"]
    send2=request.form["send2"]
    send3=request.form["send3"]
    send4=request.form["send4"]
    send5=request.form["send5"]
    send6=request.form["send6"]

    @app.route('/y_predict',methods = ["POST"])
    def y_predict():
        x_text =[[(yo) for yo in request.form.values()]]
        prediction = model1.predict(x_text)
        prediction = prediction[0]
        return render_template("secondpage.html",y=prediction)
    app.run(debug=true)
    