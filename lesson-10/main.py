# =======================================
# 🌦 Task 1 — Weather API (OpenWeatherMap)
# =======================================

import requests

API_KEY = "6a2d2f3a11527cfd6fcf8ce5a151b651"
CITY = "Tashkent"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {CITY}")
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", description)
    print("Wind Speed:", wind_speed, "m/s")
else:
    print("Error fetching data:", response.status_code)

# ========================================
# 🎬 Task 2 — Movie Recommendation System (TMDB API)
# ==========================================

import requests
import random

API_KEY = "7c144d6c63908865caa773e4867a5502"

def get_genres():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}"
    response = requests.get(url)
    return response.json()["genres"]

def recommend_movie(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    movies = response.json()["results"]

    if movies:
        movie = random.choice(movies)
        print("\n🎥 Recommended Movie:")
        print("Title:", movie["title"])
        print("Overview:", movie["overview"])
        print("Rating:", movie["vote_average"])
    else:
        print("No movies found.")

def main():
    genres = get_genres()

    print("Available Genres:")
    for g in genres:
        print(f"{g['id']} - {g['name']}")

    genre_id = input("\nEnter genre ID: ")
    recommend_movie(genre_id)

if __name__ == "__main__":
    main()

