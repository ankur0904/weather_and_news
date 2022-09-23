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
    img = myData["weather"][0]["icon"]
    return render_template("weather.html",city=cityName,data=myData,img=img)

# Search via pincode route
@app.route('/search-pincode',methods=["POST"])
def myfunction():
    pincode = request.form.get("pincode")
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={pincode}&appid={api.key1}&units=metric"
    data = requests.get(url)

    
    # Converting into python object
    myData = json.loads(data.content) 
    image = myData["weather"][0]["icon"]
    # print(img)
    return render_template("weather_pincode.html",pin=pincode,data=myData,image=image)

# News route
@app.route("/news",methods=["GET"])
def newsfun():
    
    url = (f'https://newsapi.org/v2/top-headlines?q=politics&from=2022-09-10&apiKey={api.key2}')
    response = requests.get(url)
    newsData = json.loads(response.content)
    return render_template("news.html",data=newsData["articles"])

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

