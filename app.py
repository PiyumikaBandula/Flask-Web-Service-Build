from flask import Flask, render_template, request
import requests

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/index", methods=["POST", "GET"])
def get_weatherdata():
    url="https://newsapi.org/v2/everything"
    params ={
        'q':request.form.get("keyword"),
        'apiKey':request.form.get("appid")
    }
    response=requests.get(url, params=params)
    data = response.json()  #Parse json to data
    articles=data['articles']   # Assign articles list to articles list

    return (render_template("index.html", random=articles))


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)