""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


list_labels = ["month", "day", "year", "type", "amount"]
accounting_file = "accounting/items.csv"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table = data_manager.get_table_from_file(accounting_file)

# special functions:
# ------------------

def years_net_profit(table):
    YEAR = 3
    TYPE = 4
    PROFIT = 5
    for item in table:
        if item[TYPE] == "out":
            item[PROFIT] = int(item[PROFIT])
            item[PROFIT] = -int(item[PROFIT])

    years_and_revenue = {}
    for item in table:
        if item[YEAR] not in years_and_revenue.keys():
            years_and_revenue[item[YEAR]] = int(item[PROFIT])
        else:
            years_and_revenue[item[YEAR]] += int(item[PROFIT])
    return years_and_revenue


def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    years_and_revenue = years_net_profit(table)
    for year, profit in years_and_revenue.items():
        if profit == max(years_and_revenue.values()):
            return int(year)


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    YEAR = 0
    PROFIT = 1
    years_and_revenue = years_net_profit(table)
    for item in years_and_revenue.items():
        if year == int(item[YEAR]):
            years_profit = int(item[PROFIT])

    TABLE_YEAR = 3
    CHOSEN_YEAR = 0
    ITEM_COUNTER = 1
    years_and_items = {}
    for item in table:
        if item[TABLE_YEAR] not in years_and_items.keys():
            years_and_items[item[TABLE_YEAR]] = 1
        else:
            years_and_items[item[TABLE_YEAR]] += 1
    for item in years_and_items.items():
        if year == int(item[CHOSEN_YEAR]):
            years_item_count = int(item[ITEM_COUNTER])
    return years_profit/years_item_count
