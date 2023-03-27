from flask import Flask, render_template, request
import whois

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        domain = request.form['domain']
        try:
            whois.whois(domain)
            available = False
        except whois.parser.PywhoisError:
            available = True
        return render_template('index.html', available=available, domain=domain)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
