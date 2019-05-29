from flask import Flask, render_template, request, redirect, url_for
import data_manager
import common

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

    if request.method == 'POST':
        new_record = [
            new_record.append(common.generate_random(table)),
            new_record.append(request.form.get('day')),
            new_record.append(request.form.get('month')),
            new_record.append(request.form.get('year')),
            new_record.append(request.form.get('trans_dir')),
            new_record.append(request.form.get('value'))
        ]
        data_manager.write_table_to_file('./accounting/items.csv', table)
        return redirect('/accounting')

    return render_template('add_item.html', table=table,
                           form_url=url_for('add_record'),
    page_title='Add new record', button_title='Add new record')


@app.route('/accounting/addRecord/<item_id>', methods=['GET', 'POST'])
def modify_record(item_id):
    table = data_manager.get_table_from_file('./accounting/items.csv')
    if request.method == 'POST':
        new_record = []
        new_record = [
            '''
            new_record[0] = item_id,
            new_record[1] = request.form.get('day'),
            new_record[2] = request.form.get('month'),
            new_record[3] = request.form.get('year'),
            new_record[4] = request.form.get('trans_dir'),
            new_record[5] = request.form.get('value'),
            '''
        ]
        data_manager.write_table_to_file('./accounting/items.csv', table)
        return redirect('/accounting')

    return render_template('add_item.html', table=table,
                           form_url=url_for('modify_record'),
    page_title='Modify record', button_title='Modify record')

@app.route('/crm')
def crm():
    return render_template('sub_menu.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
