import os
from dotenv import load_dotenv
import requests

# .env Datei laden
load_dotenv()

API_KEY = os.getenv('API_KEY')

API_URL = "https://api.api-ninjas.com/v1/animals?name="


def fetch_data(animal_name):
    """
    Ruft Tierdaten von der API für das gegebene 'animal_name' ab.
    Gibt eine Liste von Tieren zurück, jedes Tier ist ein Dictionary:
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
            print(f"Kein Tier mit dem Namen '{animal_name}' gefunden.")
            return []
        return data
    else:
        print(f"Fehler beim Abrufen der API-Daten: {response.status_code}")
        return []
