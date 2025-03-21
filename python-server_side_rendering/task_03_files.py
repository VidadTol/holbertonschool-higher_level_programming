from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
        items = data.get('items', [])
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id', type=int)

    if source == 'json':
        products = json_file('products.json')
    elif source == 'csv':
        products = read_csv_data('products.csv')
    else:
        return render_template('products_display.html', error = "Wrong source")

    if id:
        products = [products for product in products if product.get('id') == id]
        if not products:
            return render_template('products_display.html', error = "Product not found")

    return render_template('products_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
