import pandas as pd
import sqlite3


# ==========================================================
# MERGING AND JOINING
# ==========================================================

# 1. Inner Join on Chinook Database
print("\n=== INNER JOIN (Chinook) ===")

conn = sqlite3.connect("chinook.db")

customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)

inner_join = pd.merge(customers, invoices, on="CustomerId", how="inner")

invoice_counts = inner_join.groupby("CustomerId").size()

print(invoice_counts.head())

conn.close()


# 2. Outer Join on Movie Data
print("\n=== MOVIE JOINS ===")

movies = pd.read_csv("movie.csv")

df1 = movies[["director_name", "color"]]
df2 = movies[["director_name", "num_critic_for_reviews"]]

left_join = pd.merge(df1, df2, on="director_name", how="left")
outer_join = pd.merge(df1, df2, on="director_name", how="outer")

print("Left join rows:", len(left_join))
print("Outer join rows:", len(outer_join))


# ==========================================================
# GROUPING AND AGGREGATING
# ==========================================================

# 1. Titanic Grouped Aggregations
print("\n=== TITANIC GROUPING ===")

titanic = pd.read_excel("titanic.xlsx")

titanic_grouped = titanic.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": "sum",
    "PassengerId": "count"
}).rename(columns={"PassengerId": "Passenger_Count"})

print(titanic_grouped)


# 2. Multi-level Grouping on Movie Data
print("\n=== MOVIE MULTI GROUP ===")

movie_group = movies.groupby(["color", "director_name"]).agg({
    "num_critic_for_reviews": "sum",
    "duration": "mean"
})

print(movie_group.head())


# 3. Nested Grouping on Flights
print("\n=== FLIGHTS GROUPING ===")

flights = pd.read_parquet("flights.parquet")

flight_stats = flights.groupby(["Year", "Month"]).agg({
    "FlightNum": "count",
    "ArrDelay": "mean",
    "DepDelay": "max"
}).rename(columns={"FlightNum": "Total_Flights"})

print(flight_stats.head())


# ==========================================================
# APPLYING FUNCTIONS
# ==========================================================

# 1. Titanic Age Classification
print("\n=== TITANIC AGE GROUP ===")

def classify_age(age):
    if pd.isna(age):
        return "Unknown"
    return "Child" if age < 18 else "Adult"

titanic["Age_Group"] = titanic["Age"].apply(classify_age)

print(titanic[["Age", "Age_Group"]].head())


# 2. Normalize Employee Salaries
print("\n=== EMPLOYEE SALARY NORMALIZATION ===")

employees = pd.read_csv("employee.csv")

employees["salary_normalized"] = employees.groupby("department")["salary"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

print(employees.head())


# 3. Movie Duration Classification
print("\n=== MOVIE LENGTH CLASSIFICATION ===")

def movie_length(duration):
    if duration < 60:
        return "Short"
    elif duration <= 120:
        return "Medium"
    else:
        return "Long"

movies["length_category"] = movies["duration"].apply(movie_length)

print(movies[["movie_title", "duration", "length_category"]].head())


# ==========================================================
# USING PIPE
# ==========================================================

# 1. Titanic Pipeline
print("\n=== TITANIC PIPELINE ===")

def filter_survivors(df):
    return df[df["Survived"] == 1]

def fill_age(df):
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    return df

def fare_per_age(df):
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df

titanic_pipeline = (
    titanic
    .pipe(filter_survivors)
    .pipe(fill_age)
    .pipe(fare_per_age)
)

print(titanic_pipeline.head())


# 2. Flights Pipeline
print("\n=== FLIGHTS PIPELINE ===")

def filter_delays(df):
    return df[df["DepDelay"] > 30]

def delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / df["AirTime"]
    return df

flights_pipeline = (
    flights
    .pipe(filter_delays)
    .pipe(delay_per_hour)
)

print(flights_pipeline.head())