import json
import requests

API_URL = "https://api.api-ninjas.com/v1/animals?name=Fox"
API_KEY = "uxyIjXGBOpGHIMCkQseXjQ==Cu8jEvBxdMV5S2du"

# Daten von der API abrufen
headers = {"X-Api-Key": API_KEY}
response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    data = response.json()
else:
    print(f" Fehler beim Abrufen der API-Daten: {response.status_code}")
    exit()


# Tier-Infos serialisieren
def serialize_animal(animal_obj):
    """Serialisiert ein einzelnes Tier als HTML-Listenelement"""
    name = animal_obj.get("name", "Unknown")
    diet = animal_obj.get("characteristics", {}).get("diet", "Unknown")
    location = ", ".join(animal_obj.get("locations", ["Unknown"]))  # Falls mehrere Locations existieren
    type_ = animal_obj.get("characteristics", {}).get("type", "Unknown")

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    output += f'      <strong>Location:</strong> {location}<br/>\n'
    output += f'      <strong>Type:</strong> {type_}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'

    return output


# Alle Tiere serialisieren
output = ''.join(serialize_animal(animal) for animal in data)

# HTML-Template lesen
with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

# Platzhalter __REPLACE_ANIMALS_INFO__ ersetzen
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Neues HTML in Datei schreiben
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print("\n 'animals.html' wurde erfolgreich erstellt! Öffne die Datei im Browser.")



