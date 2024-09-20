from tkinter import *
import requests
from tkinter import messagebox
from dotenv import load_dotenv
import os

#Window
window = Tk()
window.title("Weather Application")
window.geometry("400x400")

#List of Famous Countries and Cities
country_cities = {
    "Germany": ["Berlin","Cologne","Bonn","Hamburg","Frankfurt"],
    "Turkey": ["Istanbul","Ankara","Izmir","Antalya","Bursa"],
    "England": ["London","Manchester","Liverpool","Birmingham","Leeds"],
    "Spain": ["Madrid","Barcelona","Seville","Valencia","Bilbao"],
    "Italy": ["Rome","Milan","Naples","Turin","Florence"],
    "France": ["Paris","Marseille","Lyon","Toulouse","Nice"],
    "Russia": ["Moscow","Saint Petersburg","Novosibirsk","Yekaterinburg","Nizhny Novgorod"]
}

#api_key
load_dotenv()
api_key = os.getenv("API_KEY")

#fetch weather from selected city
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            weather_label.config(text=f"Temperature in {city}: {temperature}°C\nWeather: {weather}")
        else:
            messagebox.showerror("Error","City not found. Please try another city.")
    except Exception as e:
        messagebox.showerror("Error","Unable to fetch weather data")

#Function to display top cities
def display_cities(country):
    print(f"Displaying cities for {country}")
    for widget in city_frame.winfo_children():
        widget.destroy()

    top_cities = country_cities[country]

    # Create buttons for each city
    for city in top_cities:
        print(f"Creating button for {city}")
        city_button = Button(city_frame, text=city, font=("Arial", 14), command=lambda c=city: fetch_weather(c))
        city_button.pack(pady=5)

#Country Buttons
country_frame = Frame(window)
country_frame.pack(pady=10)

Label(country_frame, text="Select a Country:", font=("Arial",16)).pack(pady=10)

for country in country_cities:
    country_button = Button(country_frame, text=country, font=("Arial", 14), command=lambda c=country: display_cities(c))
    country_button.pack(pady=5)


#Frame for city buttons
city_frame = Frame(window)
city_frame.pack(pady=20)

#weather information label
weather_label = Label(window,text="",font=("Arial",14))
weather_label.pack(pady=10)

window.mainloop()