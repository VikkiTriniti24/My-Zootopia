import os
from dotenv import load_dotenv
import requests

# Load .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

API_URL = "https://api.api-ninjas.com/v1/animals?name="


def fetch_data(animal_name):
    """
    Fetches animal data from the API for the given 'animal_name'.
    Returns a list of animals, each represented as a dictionary:
    {
      'name': ...,
      'taxonomy': {...},
      'locations': [...],
      'characteristics': {...}
    }
    """
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL + animal_name, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if not data:
            print(f"No animal found with the name '{animal_name}'.")
            return []
        return data
    else:
        print(f"Error retrieving API data: {response.status_code}")
        return []