from flask import Flask,render_template,request
import dbconn as lg
 
import pickle

app=Flask(__name__)
@app.route('/')
def front():
    return render_template('front.html')
with open('flasklinreg.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']
    print(username)
    # check if the username and password are valid
    username, password = lg.getcredentials()
    if username in username:
      if password  in password:
         return render_template('flasklinreg.html')
    else:
        # if the username and password are not valid, redirect back to the login page
        return render_template('front.html', error='Invalid username or password')

@app.route("/predicted",methods=["POST"])
def predicted():
     a = (request.form['density'])
     b = (request.form['ph'])
     c = (request.form['sulphates'])
     d = (request.form['alochol'])
     prediction = model.predict([[a,b,c,d]])[0] 
     a=round(prediction)
     print(a)
     if(a):
       return render_template("predicted.html" , quality =a)
   


if __name__ == '__main__':
    app.run(debug=True)
    