import pandas as pd
import sqlite3

# ==========================================================
# PART 1 — READING FILES
# ==========================================================

# 1. Read chinook.db customers table
print("\n--- chinook.db customers ---")

conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)

print(customers_df.head(10))

conn.close()


# 2. Read iris.json
print("\n--- iris.json ---")

iris_df = pd.read_json("iris.json")

print("Shape:", iris_df.shape)
print("Columns:", iris_df.columns)


# 3. Read titanic.xlsx
print("\n--- titanic.xlsx ---")

titanic_df = pd.read_excel("titanic.xlsx")

print(titanic_df.head())


# 4. Read flights parquet
print("\n--- flights.parquet ---")

flights_df = pd.read_parquet("flights.parquet")

print(flights_df.info())


# 5. Read movie.csv
print("\n--- movie.csv random sample ---")

movies_df = pd.read_csv("movie.csv")

print(movies_df.sample(10))


# ==========================================================
# PART 2 — EXPLORING DATAFRAMES
# ==========================================================

# 1. iris.json operations
print("\n--- IRIS DATA OPERATIONS ---")

iris_df.columns = iris_df.columns.str.lower()

iris_subset = iris_df[["sepal_length", "sepal_width"]]

print(iris_subset.head())


# 2. titanic.xlsx operations
print("\n--- TITANIC DATA OPERATIONS ---")

age_above_30 = titanic_df[titanic_df["Age"] > 30]

print("Passengers older than 30:")
print(age_above_30.head())

print("\nGender counts:")
print(titanic_df["Sex"].value_counts())


# 3. flights parquet operations
print("\n--- FLIGHTS DATA OPERATIONS ---")

flights_subset = flights_df[["origin", "dest", "carrier"]]

print(flights_subset.head())

unique_dest = flights_df["dest"].nunique()

print("Unique destinations:", unique_dest)


# 4. movie.csv operations
print("\n--- MOVIE DATA OPERATIONS ---")

long_movies = movies_df[movies_df["duration"] > 120]

sorted_movies = long_movies.sort_values(
    by="director_facebook_likes",
    ascending=False
)

print(sorted_movies.head())


# ==========================================================
# PART 3 — CHALLENGES
# ==========================================================

# 1. iris statistics
print("\n--- IRIS STATISTICS ---")

print("Mean:\n", iris_df.mean(numeric_only=True))
print("Median:\n", iris_df.median(numeric_only=True))
print("Std:\n", iris_df.std(numeric_only=True))


# 2. titanic age statistics
print("\n--- TITANIC AGE STATS ---")

print("Min age:", titanic_df["Age"].min())
print("Max age:", titanic_df["Age"].max())
print("Sum of ages:", titanic_df["Age"].sum())


# 3. movie.csv analysis
print("\n--- MOVIE ANALYSIS ---")

director_likes = movies_df.groupby("director_name")[
    "director_facebook_likes"
].sum()

top_director = director_likes.idxmax()

print("Director with highest likes:", top_director)


longest_movies = movies_df.nlargest(5, "duration")[["movie_title", "director_name", "duration"]]

print("\nTop 5 longest movies:")
print(longest_movies)


# 4. flights missing values
print("\n--- FLIGHTS MISSING VALUES ---")

print(flights_df.isnull().sum())

# Example: fill missing values in a numeric column (e.g. air_time)
if "air_time" in flights_df.columns:
    flights_df["air_time"].fillna(
        flights_df["air_time"].mean(),
        inplace=True
    )

print("Missing values handled.")