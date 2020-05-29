from flask import Flask,render_template,request
app=Flask(__name__)
s='thisisarandomstringtoeverse'
@app.route("/")
def hello():
        try:
            s=request.args.get("q")
            s=s[::-1]
        except:
            s='thisisarandomstringtoeverse'

        for i in range(100):#To increase the CPU Utilization
            x=984
            y=2245
            z=x*y

        return s

if __name__=="__main__":
        app.run(host='0.0.0.0',port=80,debug=True,threaded=True)
