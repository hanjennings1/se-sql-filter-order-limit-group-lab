import pandas as pd
import sqlite3



##### Part I: Basic Filtering #####
# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1 - RETURN ALL COLUMNS FOR PLANETS WITH 0 MOONS
df_no_moons = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
""", conn1)
# print(df_no_moons)

# STEP 2 - RETURN NAME AND MASS OF PLANETS WITH EXACTLY 7 LETTERS
df_name_seven = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7;
""", conn1)
# print(df_name_seven)


##### Part 2: Advanced Filtering #####
# STEP 3 - RETURN NAME AND MASS FOR EACH PLANET THAT HAS A MASS <= 1.00
df_mass = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00;
""", conn1)
# print(df_mass)

# STEP 4 - ALL COLUMNS FOR PLANETS WITH AT LEAST 1 MOON AND MASS < 1.00
df_mass_moon = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1 
        AND mass < 1.00;
""", conn1)
# print(df_mass_moon)

# STEP 5 - NAME AND COLOR OF PLANETS THAT HAVE COLOR CONTATINING 'BLUE'
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%';
""", conn1)
# print(df_blue)



##### Part 3: Ordering and Limiting #####
# STEP 0 - Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')
# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6 - Return the name, age, and breed of all dogs that are hungry (binary flag of 1) 
# and sort them from youngest to oldest (ASC).
df_hungry = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
""", conn2)
# print(df_hungry)

# STEP 7 - Return the name, age, and hungry columns for hungry dogs between the ages of two and seven. 
# This query should also sort these dogs in alphabetical order.
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
        AND age BETWEEN 2 and 7
    ORDER BY name ASC;
""", conn2)
# print(df_hungry_ages)

# STEP 8 - Return the name, age, and breed for the 4 oldest dogs. 
# Sort the result alphabetically based on the breed.
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC, breed ASC
    LIMIT 4;
""", conn2)
# print(df_4_oldest)



##### Part 4: Aggregation #####
# STEP 0 -  Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')
# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9 - TOTAL NUMBER OF YEARS BABE PLAYED BASEBALL PROFESSIONALLY
df_ruth_years = pd.read_sql("""
    SELECT COUNT(year) 
    FROM babe_ruth_stats; 
""", conn3)
#print(df_ruth_years)

# STEP 10 - TOTAL NUMBER OF HOMERUNS HIT
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) 
    FROM babe_ruth_stats; 
""", conn3)
# print(df_hr_total)



##### Part 5: Grouping and Aggregation #####
# STEP 11 - For each team that Babe Ruth has played on, return the team name and 
# the number of years he played on that team, aliased as 'number_years'
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(*) as number_years
    FROM babe_ruth_stats
    GROUP BY team; 
""", conn3)
# print(df_teams_years)

# STEP 12 - For each team that Babe Ruth played on and averged over 200 at bats with, 
# return the team name and average number of at bats, aliased as 'average_at_bats'.
df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING average_at_bats > 200; 
""", conn3)
# print(df_at_bats)


# CLOSE THE CONNECTION
conn1.close()
conn2.close()
conn3.close()