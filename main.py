from flask import Flask,json,render_template ,request
import requests
app = Flask(__name__)
import os
# api key = 8d7e13f0917a48a990b54a608bda9014

@app.route("/")
def home():
    response = requests.get(f"https://newsapi.org/v2/everything?q=globalaffairs&apiKey=8d7e13f0917a48a990b54a608bda9014")

    if response.status_code == 200:
        data = response.json()["articles"]  
    else:
        data = []  


    return render_template("index.html",data=data)
@app.route("/tech")
def tech():
    response = requests.get(f"https://newsapi.org/v2/everything?q=technology&apiKey=8d7e13f0917a48a990b54a608bda9014")

    if response.status_code == 200:
        data = response.json()["articles"]  
    else:
        data = []  


    return render_template("index.html",data=data)
@app.route("/entertain")
def entertain():
    response = requests.get(f"https://newsapi.org/v2/everything?q=entertainment&apiKey=8d7e13f0917a48a990b54a608bda9014")

    if response.status_code == 200:
        data = response.json()["articles"]  
    else:
        data = []  


    return render_template("index.html",data=data)
@app.route("/business")
def business():
    response = requests.get(f"https://newsapi.org/v2/everything?q=business&apiKey=8d7e13f0917a48a990b54a608bda9014")

    if response.status_code == 200:
        data = response.json()["articles"]  
    else:
        data = []  


    return render_template("index.html",data=data)
@app.route("/programming")
def programming():
    response = requests.get(f"https://newsapi.org/v2/everything?q=programming&apiKey=8d7e13f0917a48a990b54a608bda9014")

    if response.status_code == 200:
        data = response.json()["articles"]  
    else:
        data = []  


    return render_template("index.html",data=data)
@app.route("/ai")
def ai():
    response = requests.get(f"https://newsapi.org/v2/everything?q=ai&apiKey=8d7e13f0917a48a990b54a608bda9014")

    if response.status_code == 200:
        data = response.json()["articles"]  
    else:
        data = []  


    return render_template("index.html",data=data)
@app.route("/search",methods=['GET','POST'])
def search():
    if request.method == 'POST':
        search = request.form['search']
        response = requests.get(f"https://newsapi.org/v2/everything?q={search}&apiKey=8d7e13f0917a48a990b54a608bda9014")

        if response.status_code == 200:
            data = response.json()["articles"]  
        else:
            data = []  


    return render_template("index.html",data=data,search=search)
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == '__main__':
    app.run(debug=True)
