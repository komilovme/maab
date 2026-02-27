# ===============================================
# 🟢 TASK 1 — WEATHER SCRAPING (BeautifulSoup)
# ===============================================
# weather_scraper.py

from bs4 import BeautifulSoup

def task1_weather():
    with open("weather.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    rows = soup.find("tbody").find_all("tr")

    weather_data = []
    temps = []

    print("\n--- 5 Day Forecast ---")

    for row in rows:
        cols = row.find_all("td")

        day = cols[0].text.strip()
        temp_text = cols[1].text.strip()
        condition = cols[2].text.strip()

        temp_value = int(temp_text.replace("°C", ""))
        temps.append(temp_value)

        weather_data.append((day, temp_value, condition))

        print(f"{day}: {temp_value}°C - {condition}")

    # Highest temperature
    max_temp = max(temps)
    hottest_days = [d for d, t, c in weather_data if t == max_temp]

    print("\nHighest Temperature:", max_temp, "°C")
    print("Day(s):", hottest_days)

    # Sunny days
    sunny_days = [d for d, t, c in weather_data if c.lower() == "sunny"]
    print("Sunny Day(s):", sunny_days)

    # Average temperature
    avg_temp = sum(temps) / len(temps)
    print("Average Temperature:", round(avg_temp, 2), "°C")

# =================================================
# 🟢 TASK 2 — JOB SCRAPER + SQLITE (Incremental Load)
# ====================================================

# job_scraper.py

import requests
import sqlite3
from bs4 import BeautifulSoup
import csv

DB_NAME = "jobs.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
    """)

    conn.commit()
    conn.close()


def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find_all("p")[1].text.strip()
        link = job.find("a")["href"]

        # Insert or update
        cursor.execute("""
            INSERT INTO jobs (title, company, location, description, link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(title, company, location)
            DO UPDATE SET
                description=excluded.description,
                link=excluded.link
        """, (title, company, location, description, link))

    conn.commit()
    conn.close()
    print("Jobs scraped and synced.")


def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = "SELECT title, company, location FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")

    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return results


def export_to_csv(results, filename="filtered_jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location"])
        writer.writerows(results)

    print("Exported to", filename)

# ===========================================
# 🟢 TASK 3 — DEMOBLAZE LAPTOP SCRAPER → JSON
# ================================================
# demoblaze_scraper.py

import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.demoblaze.com/"

def scrape_laptops():
    laptops = []

    session = requests.Session()
    response = session.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("div", class_="card-block")

    for product in products:
        name = product.find("h4", class_="card-title").text.strip()
        price = product.find("h5").text.strip()
        description = product.find("p").text.strip()

        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })

    # Save JSON
    with open("laptops.json", "w", encoding="utf-8") as f:
        json.dump(laptops, f, indent=4)

    print("Laptops saved to laptops.json")
