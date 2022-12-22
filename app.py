"""
Main app script for Store Flask app.
"""
from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    """
    Method to generate homepage with Jinja HTML Template
    :return: Template rendered
    :rtype: str
    """
    title: str = 'Shopping Cart'
    return render_template('index.html', title=title)


@app.route('/register', methods=['GET'])
def register() -> str:
    """
    Method to register new product.
    :return: Template rendered
    :rtype: str
    """
    title: str = 'New registered product'
    return render_template('register.html', title=title)


@app.route('/products', methods=['GET'])
def products() -> str:
    """
    Method to list all products
    :return: Template rendered
    :rtype: str
    """
    title: str = 'Products list'
    return render_template('products/index.html', title=title)


@app.route('/products/create', methods=['GET'])
def create_product() -> str:
    """
    Method to create a new product
    :return: Template rendered
    :rtype: str
    """
    return render_template('products/create.html')


if __name__ == '__main__':
    app.run(debug=True)
