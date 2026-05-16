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
            "May": {"budget": 70, "mid_range": 160, "luxury": 420},
            "June": {"budget": 75, "mid_range": 170, "luxury": 450},
            "July": {"budget": 90, "mid_range": 210, "luxury": 520},
            "August": {"budget": 100, "mid_range": 230, "luxury": 580},
        },

        "Paris": {
            "May": {"budget": 80, "mid_range": 180, "luxury": 500},
            "June": {"budget": 85, "mid_range": 200, "luxury": 550},
            "July": {"budget": 95, "mid_range": 240, "luxury": 620},
            "August": {"budget": 100, "mid_range": 250, "luxury": 650},
        },

        "Dubai": {
            "May": {"budget": 60, "mid_range": 140, "luxury": 380},
            "June": {"budget": 55, "mid_range": 130, "luxury": 350},
            "July": {"budget": 50, "mid_range": 120, "luxury": 320},
            "August": {"budget": 50, "mid_range": 120, "luxury": 310},
        },

        "New York": {
            "May": {"budget": 110, "mid_range": 260, "luxury": 700},
            "June": {"budget": 120, "mid_range": 280, "luxury": 760},
            "July": {"budget": 140, "mid_range": 320, "luxury": 850},
            "August": {"budget": 145, "mid_range": 330, "luxury": 900},
        },

        "Sydney": {
            "May": {"budget": 75, "mid_range": 170, "luxury": 430},
            "June": {"budget": 70, "mid_range": 160, "luxury": 400},
            "July": {"budget": 68, "mid_range": 150, "luxury": 390},
            "August": {"budget": 72, "mid_range": 155, "luxury": 410},
        }
    }

    if city_name not in hotel_db:
        return {"error": "City not found"}

    return hotel_db[city_name].get(month, {"error": "Month not found"})