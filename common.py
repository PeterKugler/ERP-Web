""" Common module
implement commonly used functions here
"""

import random


def generate_random_letter_number_spec_char(letter1, letter2):
    return chr(random.randint(ord(letter1), ord(letter2)))


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    while generated == '':
        for i in range(2):
            generated += generate_random_letter_number_spec_char("a", "z")
            generated += generate_random_letter_number_spec_char("A", "Z")
            generated += generate_random_letter_number_spec_char("0", "9")
            generated += generate_random_letter_number_spec_char("!", "/")

        if generated not in table:
            return generated
        else:
            generated = ''
            continue



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