from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json')
    data = response.json()
    products = pd.DataFrame(data['products']).T
    products = products.sort_values(by='popularity', ascending=False)
    return render_template('index.html', tables=[products.to_html(classes='data')], titles=products.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
