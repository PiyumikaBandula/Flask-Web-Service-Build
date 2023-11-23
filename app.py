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
    data = response.json()
    status = data['status']
    results=data['totalResults']
    articles=data['articles']
    s=''
    for i in range(len(articles)):
        if articles[i][request.form.get("info")]:
            s += "<div><p>" + articles[i][request.form.get("info")] + "</p></div>"
    return (f"<div><p>status : {status} </p></div>"
            f"<div><p>totalResults: {results} </p></div>"
            f"<div><p>{s}</p></div>")


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)