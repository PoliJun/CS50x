# Lecture 7 SQL

## flat-file database

-   csv file
-   csv.reader(file)
    > This returns list
-   csv.DictReader(file)
    > This returns Dictionary
-   code sample

    ```python
    import csv

    with open("favorites.csv", "r") as file:
        reader = csv.DictReader(file)
        counts = {}
        for row in reader:
            favorite = row["language"]
            if favorite in counts:
                counts[favorite] += 1
            else:
                counts[favorite] = 1


    def get_value(language):
        return counts[language]


    # sorted(): Sorted by alphabetically, and a lambda function
    # """ this would order as increasing numbers """
    for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
        print(f"{favorite}: {counts[favorite]}")
    ```

-   lambda function
    ```python
    key = lambda favorite: counts[favorite]
    ```

## relational database

SQL

## CRUD

-   C: creating data
    -   CREATE
    -   INSERT
-   R: reading data
    -   SELECT
-   U: updating data
    -   UPDATE
-   D: deleting data
    -   DELETE
    -   DROP

## Syntax and Statements

-   DISTINCT, COUNT, SELECT
    -   `SELECT * FROM favorites;`
    -   `SELECT COUNT(*) FROM favorites ;`
    -   `SELECT DISTINCT(language) FROM favorites;`
    -   `SELECT COUNT(DISTINCT(language)) FROM favorites;`
-   WHERE
-   LIKE
-   ORDER BY
-   LIMIT: show limited numbers of rows
-   GROUP BY: `SELECT language, count(*) FROM favorites GROUP BY language;`
-   INSERT: `INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville')`
-   UPDATE: `UPDATE favorites SET language = 'SQL' WHERE language = 'C';`
    > It is dangerous to use `UPDATE` without `WHERE` clause
-   DELETE:
    -   `DELETE FROM favorites;` This will delete all data

## Data Types

-   BLOB
-   INTEGER
-   NUMERIC
-   REAL
-   TEXT

## Constraints

-   NOT NULL
-   UNIQUE

## key words

-   Primary key
-   Foreign key
-   Join

## JOIN

-   select multiple tables is slower than join

## tips

-   `%`: `SELEET name from stars where name like 'Steve C%';`

## indexes

`CREATE INDEX name_index ON table (column, ...);`. After creating indexes, the select query will be executed much more faster.

-   B-trees: more efficient than binary tree

## execute sql queries via Python

```python
from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")

# this returns a list of dictionaries
rows = db.execute(
    "SELECT COUNT(*) AS n FROM favorites WHERE problem = 'Mario'")

row = rows[0]
print(row["n"])
```
