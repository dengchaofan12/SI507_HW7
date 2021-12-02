from flask import Flask, render_template
import requests
import secrets

from requests.models import Response

key = secrets.api_key


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome!<h1>' 

@app.route('/name/<name>')
def hello_name(name):
    return render_template('name.html', name=name)

@app.route('/headlines/<name>')
def find_titles(name):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
    params = {"api-key": key}
    response = requests.get(url, params).json()
    titles = []
    url_list = []
    for item in response["results"]:
        titles.append(item["title"])
        url_list.append(item["url"])
    return render_template('headline.html',name=name, list=titles, url_list=url_list)   

@app.route('/image/<name>')
def find_titles_with_image(name):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
    params = {"api-key": key}
    response = requests.get(url, params).json()
    titles = []
    url_list = []
    image_list = []
    for item in response["results"]:
        titles.append(item["title"])
        url_list.append(item["url"])
        image_list.append(item["multimedia"][0]["url"])
    return render_template('image.html',name=name, list=titles, url_list=url_list, image_list=image_list)  

if __name__ == '__main__':  
    app.run()
