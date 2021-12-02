from flask import Flask, render_template
import secrets
import requests
client_key = secrets.api_key
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm2>')
def find_stroies(nm2):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {"api-key": client_key}
    results = requests.get(base_url, params).json()
    ls_title = []
    for i in results["results"]:
        ls_title.append(i["title"])
    return render_template('stories.html',name=nm2, title_list=ls_title)
if __name__ == '__main__':  
    app.run(debug=True)