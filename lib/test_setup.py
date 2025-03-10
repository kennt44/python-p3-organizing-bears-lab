import sys, os
# Add the current directory of the script to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import sqlite3
from lib.sql_queries import *  # Importing the queries

def test_select_all_female_bears_return_name_and_age():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Create table and insert data
    with open('lib/create.sql') as f:
        cursor.executescript(f.read())
    with open('lib/insert.sql') as f:
        cursor.executescript(f.read())

    # Test the query
    cursor.execute(select_all_female_bears_return_name_and_age)
    results = cursor.fetchall()
    assert len(results) == 3, "There should be 3 female bears"
    assert results[0] == ('Tabitha', 4), "The first female bear should be Tabitha with age 4"

    connection.close()

def test_select_all_alive_bears():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Create table and insert data
    with open('lib/create.sql') as f:
        cursor.executescript(f.read())
    with open('lib/insert.sql') as f:
        cursor.executescript(f.read())

    # Test the query
    cursor.execute(select_all_alive_bears)
    results = cursor.fetchall()
    assert len(results) == 7, "There should be 7 alive bears"

    connection.close()

def test_select_oldest_bear_name():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Create table and insert data
    with open('lib/create.sql') as f:
        cursor.executescript(f.read())
    with open('lib/insert.sql') as f:
        cursor.executescript(f.read())

    # Test the query
    cursor.execute(select_oldest_bear_name)
    result = cursor.fetchone()
    assert result == ('Grinch',), "The oldest bear should be 'Grinch'"

    connection.close()

def test_select_bears_with_playful_temperament():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Create table and insert data
    with open('lib/create.sql') as f:
        cursor.executescript(f.read())
    with open('lib/insert.sql') as f:
        cursor.executescript(f.read())

    # Test the query
    cursor.execute(select_bears_with_playful_temperament)
    results = cursor.fetchall()
    assert len(results) == 1, "There should be 1 playful bear"
    assert results[0] == ('Rowdy',), "The playful bear should be Rowdy"

    connection.close()

def test_select_not_alive_bears():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Create table and insert data
    with open('lib/create.sql') as f:
        cursor.executescript(f.read())
    with open('lib/insert.sql') as f:
        cursor.executescript(f.read())

    # Test the query
    cursor.execute(select_not_alive_bears)
    results = cursor.fetchall()
    assert len(results) == 1, "There should be 1 dead bear"
    assert results[0] == ('Grinch',), "The dead bear should be 'Grinch'"

    connection.close()
