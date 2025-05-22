import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.github.com')
    return f'GitHub API Status: {response.status_code}'

if __name__ == '__main__':
    app.run(debug=True)
