# lib/sql_queries.py

# Query to select all female bears' names and ages
select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex = 'F';
"""

# Query to select all bears that are alive
select_all_alive_bears = """
    SELECT
        bears.name
    FROM bears
    WHERE alive = 1;
"""

# Query to select the name of the oldest bear
select_oldest_bear_name = """
    SELECT
        bears.name
    FROM bears
    ORDER BY bears.age DESC
    LIMIT 1;
"""

# Query to select bears with a specific temperament (e.g., 'Playful')
select_bears_with_playful_temperament = """
    SELECT
        bears.name
    FROM bears
    WHERE bears.temperament = 'Playful';
"""

# Query to select bears that are not alive
select_not_alive_bears = """
    SELECT
        bears.name
    FROM bears
    WHERE alive = 0;
"""
