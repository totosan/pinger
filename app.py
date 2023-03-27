from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.get_text()[:100]
            available = True
        except:
            content = ''
            available = False
        return f'''
            <p>The first 100 characters of {url}:</p>
            <pre>{content}</pre>
            ''' if available else f'<p>The URL {url} could not be accessed.</p>'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
