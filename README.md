# Lab: Filtering, Ordering, Limiting, and Grouping Data with SQL

**Completed Sept 21, 2026** 

## Overview

This lab practices writing SQL queries with `sqlite3` and `pandas`. All queries are in `main.py`, and the test suite is used for grading.

| Database | Table | Contents |
|---|---|---|
| `planets.db` | `planets` | Planets in our solar system |
| `dogs.db` | `dogs` | Famous fictional dogs |
| `babe_ruth.db` | `babe_ruth_stats` | Babe Ruth's season-by-season hitting stats |

## Setup

```bash
pipenv install
pipenv shell
python3 main.py
pytest
```

Use `pytest -x` to stop at the first failing test.

To check a query's output, uncomment the `print(...)` line below that step in `main.py` (for example, `# print(df_no_moons)`) and run `python3 main.py`. Each step has one, and they are commented out by default so the output stays clean.

## Concepts Covered

| Part | Topic | Key SQL |
|---|---|---|
| 1 | Basic filtering | `WHERE`, `LENGTH()` |
| 2 | Advanced filtering | `<=`, `<`, `AND`, `LIKE '%...%'` |
| 3 | Ordering and limiting | `ORDER BY` (`ASC`/`DESC`), `BETWEEN`, `LIMIT` |
| 4 | Aggregation | `COUNT`, `SUM` |
| 5 | Grouping and aggregation | `GROUP BY`, aliases, `HAVING` |

## Clause Order

1. `SELECT`
2. `FROM`
3. `WHERE` (filters rows, before grouping)
4. `GROUP BY`
5. `HAVING` (filters groups, after aggregating)
6. `ORDER BY`
7. `LIMIT`

## Notes

- **Step 8:** The instructions say to sort the 4 oldest dogs alphabetically by breed, but the test expects them in age order. The solution sorts by `age DESC, breed ASC` with `LIMIT 4` to match the test.
- **Connections:** `conn1.close()`, `conn2.close()`, and `conn3.close()` stay at the bottom of `main.py`, below all queries.