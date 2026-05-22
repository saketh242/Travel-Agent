# fake api endpoints/tools
from crewai.tools import tool

# -----------------------------------
# Fake Weather API
# -----------------------------------
@tool
def get_weather_data(city_name: str, month: str) -> dict:
    """
    Mock API:
    Returns weather data for a given city and month.
    """

    weather_db = {

        "Tokyo": {
            "January": {"temp": 6, "condition": "Cool"},
            "February": {"temp": 7, "condition": "Cool"},
            "March": {"temp": 11, "condition": "Mild"},
            "April": {"temp": 16, "condition": "Spring"},
            "May": {"temp": 22, "condition": "Pleasant"},
            "June": {"temp": 26, "condition": "Humid"},
            "July": {"temp": 31, "condition": "Hot & Humid"},
            "August": {"temp": 33, "condition": "Very Hot"},
            "September": {"temp": 28, "condition": "Rainy"},
            "October": {"temp": 22, "condition": "Cool"},
            "November": {"temp": 17, "condition": "Chilly"},
            "December": {"temp": 11, "condition": "Cold"},
        },

        "Paris": {
            "January": {"temp": 5, "condition": "Cold"},
            "February": {"temp": 6, "condition": "Cool"},
            "March": {"temp": 9, "condition": "Overcast"},
            "April": {"temp": 12, "condition": "Breezy"},
            "May": {"temp": 18, "condition": "Pleasant"},
            "June": {"temp": 22, "condition": "Warm"},
            "July": {"temp": 26, "condition": "Sunny"},
            "August": {"temp": 27, "condition": "Warm"},
            "September": {"temp": 23, "condition": "Cool"},
            "October": {"temp": 17, "condition": "Rainy"},
            "November": {"temp": 11, "condition": "Cold"},
            "December": {"temp": 7, "condition": "Freezing"},
        },

        "Dubai": {
            "January": {"temp": 21, "condition": "Warm"},
            "February": {"temp": 24, "condition": "Warm"},
            "March": {"temp": 28, "condition": "Hot"},
            "April": {"temp": 33, "condition": "Very Hot"},
            "May": {"temp": 38, "condition": "Very Hot"},
            "June": {"temp": 41, "condition": "Extreme Heat"},
            "July": {"temp": 44, "condition": "Scorching"},
            "August": {"temp": 45, "condition": "Dry Heat"},
            "September": {"temp": 41, "condition": "Hot"},
            "October": {"temp": 35, "condition": "Warm"},
            "November": {"temp": 29, "condition": "Pleasant"},
            "December": {"temp": 24, "condition": "Cool"},
        },

        "New York": {
            "January": {"temp": 1, "condition": "Freezing"},
            "February": {"temp": 3, "condition": "Cold"},
            "March": {"temp": 8, "condition": "Windy"},
            "April": {"temp": 14, "condition": "Showers"},
            "May": {"temp": 20, "condition": "Pleasant"},
            "June": {"temp": 26, "condition": "Warm"},
            "July": {"temp": 31, "condition": "Hot"},
            "August": {"temp": 30, "condition": "Humid"},
            "September": {"temp": 25, "condition": "Comfortable"},
            "October": {"temp": 18, "condition": "Cool"},
            "November": {"temp": 11, "condition": "Cold"},
            "December": {"temp": 5, "condition": "Snowy"},
        },

        "Sydney": {
            "January": {"temp": 29, "condition": "Hot"},
            "February": {"temp": 28, "condition": "Hot"},
            "March": {"temp": 26, "condition": "Warm"},
            "April": {"temp": 23, "condition": "Mild"},
            "May": {"temp": 19, "condition": "Cool"},
            "June": {"temp": 16, "condition": "Chilly"},
            "July": {"temp": 14, "condition": "Cold"},
            "August": {"temp": 15, "condition": "Windy"},
            "September": {"temp": 18, "condition": "Pleasant"},
            "October": {"temp": 22, "condition": "Warm"},
            "November": {"temp": 25, "condition": "Sunny"},
            "December": {"temp": 28, "condition": "Hot"},
        }
    }

    if city_name not in weather_db:
        return {"error": "City not found"}

    return weather_db[city_name].get(month, {
        "error": "Month not found"
    })


# -----------------------------------
# Fake Flight Price API
# -----------------------------------
@tool
def get_flight_prices(city_name: str, month:str) -> dict:
    """
    Mock API:
    Returns hardcoded round-trip flight prices.
    """

    flight_db = {

        "Tokyo": {
            "January": 920,
            "February": 890,
            "March": 850,
            "April": 800,
            "May": 780,
            "June": 820,
            "July": 950,
            "August": 1100,
            "September": 870,
            "October": 760,
            "November": 720,
            "December": 980
        },

        "Paris": {
            "January": 700,
            "February": 680,
            "March": 650,
            "April": 630,
            "May": 650,
            "June": 700,
            "July": 850,
            "August": 900,
            "September": 750,
            "October": 680,
            "November": 620,
            "December": 890
        },

        "Dubai": {
            "January": 380,
            "February": 390,
            "March": 410,
            "April": 430,
            "May": 400,
            "June": 420,
            "July": 500,
            "August": 550,
            "September": 470,
            "October": 430,
            "November": 390,
            "December": 600
        },

        "New York": {
            "January": 980,
            "February": 940,
            "March": 900,
            "April": 860,
            "May": 900,
            "June": 950,
            "July": 1200,
            "August": 1300,
            "September": 980,
            "October": 920,
            "November": 870,
            "December": 1400
        },

        "Sydney": {
            "January": 1450,
            "February": 1400,
            "March": 1300,
            "April": 1200,
            "May": 1000,
            "June": 1100,
            "July": 1250,
            "August": 1350,
            "September": 1150,
            "October": 1050,
            "November": 990,
            "December": 1500
        }
    }

    if city_name not in flight_db:
        return {"error": "City not found"}

    price = flight_db[city_name].get(month)

    if not price:
        return {"error": "Month not found"}

    return {
        "city": city_name,
        "month": month,
        "round_trip_price_usd": price
    }


# -----------------------------------
# Fake Tourist Places API
# -----------------------------------
@tool
def get_tourist_places(city_name: str) -> list:
    """
    Mock API:
    Returns top 5 tourist places in a city.
    """

    places_db = {

        "Tokyo": [
            "Shibuya Crossing",
            "Tokyo Tower",
            "Senso-ji Temple",
            "Akihabara",
            "Mount Fuji"
        ],

        "Paris": [
            "Eiffel Tower",
            "Louvre Museum",
            "Notre Dame",
            "Arc de Triomphe",
            "Seine River Cruise"
        ],

        "Dubai": [
            "Burj Khalifa",
            "Dubai Mall",
            "Palm Jumeirah",
            "Desert Safari",
            "Dubai Marina"
        ],

        "New York": [
            "Times Square",
            "Central Park",
            "Statue of Liberty",
            "Brooklyn Bridge",
            "Empire State Building"
        ],

        "Sydney": [
            "Sydney Opera House",
            "Bondi Beach",
            "Harbour Bridge",
            "Taronga Zoo",
            "Blue Mountains"
        ]
    }

    return places_db.get(city_name, {
        "error": "City not found"
    })


# -----------------------------------
# Fake Hotel Price API
# -----------------------------------
@tool
def get_hotel_prices(city_name: str, month: str) -> dict:
    """
    Mock API:
    Returns hotel prices for a given city and month.
    """

    hotel_db = {

        "Tokyo": {
            "January": {"budget": 60, "mid_range": 140, "luxury": 380},
            "February": {"budget": 62, "mid_range": 145, "luxury": 390},
            "March": {"budget": 65, "mid_range": 150, "luxury": 400},
            "April": {"budget": 68, "mid_range": 155, "luxury": 410},
            "May": {"budget": 70, "mid_range": 160, "luxury": 420},
            "June": {"budget": 75, "mid_range": 170, "luxury": 450},
            "July": {"budget": 90, "mid_range": 210, "luxury": 520},
            "August": {"budget": 100, "mid_range": 230, "luxury": 580},
            "September": {"budget": 95, "mid_range": 220, "luxury": 540},
            "October": {"budget": 85, "mid_range": 190, "luxury": 470},
            "November": {"budget": 78, "mid_range": 170, "luxury": 430},
            "December": {"budget": 74, "mid_range": 165, "luxury": 410},
        },

        "Paris": {
            "January": {"budget": 85, "mid_range": 190, "luxury": 520},
            "February": {"budget": 83, "mid_range": 185, "luxury": 510},
            "March": {"budget": 82, "mid_range": 182, "luxury": 505},
            "April": {"budget": 84, "mid_range": 188, "luxury": 515},
            "May": {"budget": 80, "mid_range": 180, "luxury": 500},
            "June": {"budget": 85, "mid_range": 200, "luxury": 550},
            "July": {"budget": 95, "mid_range": 240, "luxury": 620},
            "August": {"budget": 100, "mid_range": 250, "luxury": 650},
            "September": {"budget": 92, "mid_range": 230, "luxury": 600},
            "October": {"budget": 88, "mid_range": 210, "luxury": 560},
            "November": {"budget": 82, "mid_range": 195, "luxury": 530},
            "December": {"budget": 90, "mid_range": 210, "luxury": 580},
        },

        "Dubai": {
            "January": {"budget": 55, "mid_range": 120, "luxury": 330},
            "February": {"budget": 58, "mid_range": 125, "luxury": 340},
            "March": {"budget": 60, "mid_range": 130, "luxury": 350},
            "April": {"budget": 58, "mid_range": 128, "luxury": 345},
            "May": {"budget": 60, "mid_range": 140, "luxury": 380},
            "June": {"budget": 55, "mid_range": 130, "luxury": 350},
            "July": {"budget": 50, "mid_range": 120, "luxury": 320},
            "August": {"budget": 50, "mid_range": 120, "luxury": 310},
            "September": {"budget": 52, "mid_range": 125, "luxury": 330},
            "October": {"budget": 56, "mid_range": 130, "luxury": 340},
            "November": {"budget": 58, "mid_range": 135, "luxury": 360},
            "December": {"budget": 62, "mid_range": 140, "luxury": 370},
        },

        "New York": {
            "January": {"budget": 100, "mid_range": 240, "luxury": 650},
            "February": {"budget": 105, "mid_range": 250, "luxury": 680},
            "March": {"budget": 108, "mid_range": 255, "luxury": 690},
            "April": {"budget": 110, "mid_range": 260, "luxury": 700},
            "May": {"budget": 110, "mid_range": 260, "luxury": 700},
            "June": {"budget": 120, "mid_range": 280, "luxury": 760},
            "July": {"budget": 140, "mid_range": 320, "luxury": 850},
            "August": {"budget": 145, "mid_range": 330, "luxury": 900},
            "September": {"budget": 135, "mid_range": 310, "luxury": 820},
            "October": {"budget": 125, "mid_range": 290, "luxury": 780},
            "November": {"budget": 115, "mid_range": 270, "luxury": 720},
            "December": {"budget": 130, "mid_range": 310, "luxury": 860},
        },

        "Sydney": {
            "January": {"budget": 90, "mid_range": 210, "luxury": 520},
            "February": {"budget": 88, "mid_range": 205, "luxury": 510},
            "March": {"budget": 85, "mid_range": 200, "luxury": 500},
            "April": {"budget": 80, "mid_range": 185, "luxury": 460},
            "May": {"budget": 75, "mid_range": 170, "luxury": 430},
            "June": {"budget": 70, "mid_range": 160, "luxury": 400},
            "July": {"budget": 68, "mid_range": 150, "luxury": 390},
            "August": {"budget": 72, "mid_range": 155, "luxury": 410},
            "September": {"budget": 76, "mid_range": 165, "luxury": 430},
            "October": {"budget": 80, "mid_range": 175, "luxury": 450},
            "November": {"budget": 83, "mid_range": 180, "luxury": 470},
            "December": {"budget": 88, "mid_range": 200, "luxury": 500},
        }
    }

    if city_name not in hotel_db:
        return {"error": "City not found"}

    return hotel_db[city_name].get(month, {"error": "Month not found"})