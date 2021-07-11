import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=jsonObj['a']
    b=jsonObj['b']
    c=jsonObj['c']
            
    f1=float(a)+float(b)+float(c)
    f2=(float(a)*float(b))/float(c)
    
    response+="<b> Sum of a, b, c is <b>"+str(f1)+"</b><br>"
    response+="<b> (a*b)/c is <b>"+str(f2)+"</b><br>"
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
