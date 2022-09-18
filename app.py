from flask import Flask, render_template, request
from newsapi import NewsApiClient
import requests
import json
import api

app = Flask(__name__)

# Home route
@app.route('/',methods=["GET"])
def my_app():
    return render_template('index.html')

# Search via city name route
@app.route('/search',methods=["POST"])
def myfun():
    cityName = request.form.get("cityName")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api.key1}&units=metric"
    data = requests.get(url)
    
    # Converting into python object
    myData = json.loads(data.content)
    return render_template("weather.html",city=cityName,data=myData)

# Search via pincode route
@app.route('/search-pincode',methods=["POST"])
def myfunction():
    pincode = request.form.get("pincode")
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={pincode}&appid={api.key1}&units=metric"
    data = requests.get(url)

    # Converting into python object
    myData = json.loads(data.content)  
    return render_template("weather_pincode.html",pin=pincode,data=myData)

# News route
@app.route("/news",methods=["GET"])
def newsfun():
    
    url = (f'https://newsapi.org/v2/top-headlines?q=politics&from=2022-09-10&apiKey={api.key2}')
    response = requests.get(url)
    newsData = json.loads(response.content)
    return render_template("news.html",data=newsData["articles"])
