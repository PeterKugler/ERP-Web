from flask import Flask, render_template, request, redirect, url_for
import data_manager
import common
import copy


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main_menu.html')


@app.route('/accounting')
def accounting():
    table = data_manager.get_table_from_file('./accounting/items.csv')
    table_func = copy.deepcopy(table)
    max_profit = common.which_year_max(table_func)
    #avg_profit_year_result = common.avg_amount(table, year)
    return render_template('accounting.html', table=table, max_profit=max_profit)


@app.route('/accounting/addRecord', methods=['GET', 'POST'])
def add_record():
    table = data_manager.get_table_from_file('./accounting/items.csv')

    if request.method == 'POST':
        new_record = []
        new_record.append(common.generate_random(table)),
        new_record.append(request.form.get('day')),
        new_record.append(request.form.get('month')),
        new_record.append(request.form.get('year')),
        new_record.append(request.form.get('trans_dir')),
        new_record.append(request.form.get('value'))

        table.append(new_record)
        data_manager.write_table_to_file('./accounting/items.csv', table)
        return redirect('/accounting')

    return render_template('add_item.html', table=table,
                           form_url=url_for('add_record'),
    page_title='Add new record', button_title='Add new record')


@app.route('/accounting/modRecord/<item_id>', methods=['GET', 'POST'])
def modify_record(item_id):
    table = data_manager.get_table_from_file('./accounting/items.csv')

    if request.method == 'GET':
        for item in table:
            if item_id in item:
                record = item

    if request.method == 'POST':
        for record in table:
            if item_id in record:
                record_index = table.index(record)
                table.remove(record)
                record[0] = item_id
                record[1] = request.form.get('day')
                record[2] = request.form.get('month')
                record[3] = request.form.get('year')
                record[4] = request.form.get('trans_dir')
                record[5] = request.form.get('value')
                table.insert(record_index, record)

        data_manager.write_table_to_file('./accounting/items.csv', table)
        return redirect('/accounting')

    return render_template('modify.html', table=table,
                           form_url=url_for('modify_record', item_id=item_id),
    page_title='Modify record', button_title='Modify record', record=record)


@app.route('/accounting/delRecord/<item_id>', methods=['GET', 'POST'])
def del_record(item_id):
    table = data_manager.get_table_from_file('./accounting/items.csv')

    if request.method == 'POST':
        for item in table:
            if item_id in item:
                table.remove(item)

        data_manager.write_table_to_file('./accounting/items.csv', table)
        return redirect('/accounting')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
