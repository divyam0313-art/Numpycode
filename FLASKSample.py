from flask import Flask,jsonify,request,render_template_string


app = Flask(__name__)

@app.route("/getsquare",methods=["GET"])
def getsquare():
    number=request.args.get('number',default=0,type=int)
    result=number**2
    return jsonify(result)

@app.route("/greet/<name>")
def greetuser(name):
    return render_template_string('<h1>Hello, {{name}}!</h1>' ,name=name)


@app.route("/postsquare",methods=["post"])
def postsquare():
    """data= jsonify({"name":"divya","age":32})"""
    jsondata=request.get_json()
    print(jsondata)

@app.route("/submitForm",methods=["GET","POST"])
def submitformdata():
    if(request.method=="POST"):
       message=request.form.get("message")
       """data=request.get_json()
       message=data.get("message")"""
       return render_template_string("<H1>the message is {{message}}</H1>",message=message)
    else:
        return '''
                <form method="POST" action="/submitForm">
                    <input type="text" name="message" />
                    <input type="submit" /> 
                    </form>              
                '''
    


if __name__=='__main__':
    app.run() 

"""CURL Command to test the API:"""
# curl -X POST -H "Content-Type: application/json" -d '{"number":5}' http://localhost:5000/POST-DATA

