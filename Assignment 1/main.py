import requests
import pandas as pd

response = requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json')
data = response.json()

products = pd.DataFrame(data['products']).T

products = products.sort_values(by='popularity', ascending=False)
print(products[['title', 'price']])
