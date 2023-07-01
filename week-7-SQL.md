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

-   place holder: `?`
    > `rows = db.execute("SELECT * FROM favorites WHERE problem = ?", favorite)`  
    > **Don't use {favorite}, this would lead you to a hack if you trust what people input**

## multi access

-   BEGIN TRANSACTION
-   COMMIT
-   ROLLBACK

## SQL injection attack

> **Don't use {favorite}, this would lead you to a hack if you trust what people input**

# Section 7

-   `.schema`
-   SELECT
-   WHERE
-   LIKE: `WHERE student_name  LIKE "%Potter";`

## Statements

**You should always capitalize your SQL key words like `SELECT`**

-   Find the names and houses of students whose names begin with "H".
    > `SELECT student_name, house FROM students WHERE student_name LIKE "H%";`  
    > Yes, that's correct. In SQL, values after `=` is **case sensitive** and values after `LIKE` is **not** case sensitive¹. However, you can make your query case sensitive by making use of the `COLLATE` keyword. For example, you can write a query like this: `SELECT A FROM MyTbl WHERE A COLLATE Latin1_General_CS_AS = 'ABCdef'` to get the result in case-sensitive manner.
-   ORDER BY
    > `ASC` and `DESC`: ascending and descending.  
    > `SELECT student_name, house FROM students WHERE student_name LIKE "H%" ORDER BY student_name, house ACS`  
    > `SELECT house, COUNT(*) FROM students GROUP BY house;`  
    > in the above, first sort _student_name_ then sort _house_
-   LIMIT
    > Show the first limited number of results  
    > `SELECT * FROM students WHERE student_name LIKE "H%" ORDER BY student_name LIMIT 10;`
-   AS
    > `SELECT COUNT(*) AS number_of_students FROM students;`

## Database Design

student_name, house_name, head
the house repeatedly, so we create a new table of house.

### Design Principles

-   Each table should be a collection of a **single entity**.
-   For example, we should have a different table for each of students, house, and student-house assignments.

    > The primary key of the assignments: ?  
    > The primary key is inside of the current table, the foreing key is reference to another table.  
    > **If there's not an assignment table, if I want change the name of a house, it would be a heavy work.**

-   data types
    -   INTEGER
    -   TEXT
    -   ...
-   constraints
    -   NOT NULL
    -   ...
-   JOIN
    > `SELECT house, COUNT(student_id) FROM assignments JOIN house ON house.id = assignments.house_id;`

# Shorts

## SQL

**The Structured Query Language**

-   CHAR and VARCHAR
    > Unlike C, CHAR(10) always store 10 memmories, VARCHAR(99) store 1,2,3,4,5... up to 99 memories.
-   choose the right primary key, make sure it is **unique**
-   ID number, which is the primary key, should set it autoincrement

## SELECT

-   Extract information from a table.
    > `SELECT <columns> FROM <table> WHERE <predicate> ORDER BY <column>` > `*` : every column
-   SELECT(JOIN)
    -   Extract information from multiple tables
        > `SELECT users.fullname, moms.mother FROM users JOIN moms ON users.username = moms.username`
-   UPDATE
    > Modify information in a table.  
    > `UPDATE <table> SET <column> = <value> WHERE <predicate>;`
-   DELETE
    > Remove information from a table  
    > `DELETE FROM users WHERE <predicate>;`
