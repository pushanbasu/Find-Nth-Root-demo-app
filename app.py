from flask import Flask, render_template, request, jsonify
app=Flask(__name__)

@app.route('/',methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/findNthRoot',methods=['POST'])
def result():
    if request.method=='POST':
        try:
            number=float(request.form['num'])
            n=float(request.form['n'])
            if n!=0:
                nthRoot = number ** (1 / n)
                #return jsonify({'{}th Root of {} '.format(n,number):nthRoot})
                return render_template('result.html',num=number,pow=n,rootVal=nthRoot)

            else:
                return "MathERROR! 'N' can not be zero. "
        except Exception as e:
            return e





if __name__ == '__main__':
    app.run(debug=True)
