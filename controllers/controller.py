from flask import render_template
from app import app
from models.order_list import book_orders

@app.route('/orders')
def index():
    return render_template('index.html', all_orders=book_orders)

@app.route('/orders/<int:index_number>')
def single_order(index_number):
    return render_template('order.html', book_orders = book_orders[index_number])


