from flask import Flask, request, render_template
import pandas as pd
import numpy as np

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="GET":
        return render_template('index.html')

    else:
        number=int(request.form['number'])
        ans=""

        if(number%2==0) : ans="EVEN"
        else : ans="ODD"

        return render_template('result.html',ans=ans,number=number)

if __name__=="__main__":
    app.run(debug=True)