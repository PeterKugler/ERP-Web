from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main_menu.html')


@app.route('/accounting')
def accounting():
    table = data_manager.get_table_from_file('./accounting/items.csv')
    return render_template('accounting.html', table=table)


@app.route('/accounting/addRecord', methods=['GET', 'POST'])
def add_record():
    table = data_manager.get_table_from_file('./accounting/items.csv')
    return render_template('add_item.html', table=table)


@app.route('/crm')
def crm():
    return render_template('sub_menu.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
