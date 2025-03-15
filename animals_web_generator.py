import json
import data_fetcher


def serialize_animal(animal_obj):
    """Serialisiert ein einzelnes Tier als HTML-Listenelement"""
    name = animal_obj.get("name", "Unknown")
    diet = animal_obj.get("characteristics", {}).get("diet", "Unknown")
    location = ", ".join(animal_obj.get("locations", ["Unknown"]))
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


# Benutzer nach einem Tier fragen
animal_name = input("Please enter an animal: ").strip()

# Daten abrufen (von `data_fetcher.py`)
data = data_fetcher.fetch_data(animal_name)

if not data:
    print(f"Keine Daten für '{animal_name}' gefunden. Beende Programm.")
    exit()

# lle Tiere serialisieren
output = ''.join(serialize_animal(animal) for animal in data)

# HTML-Template lesen
with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

# Platzhalter __REPLACE_ANIMALS_INFO__ ersetzen
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Neues HTML in Datei schreiben
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print(f"\n Website für '{animal_name}' wurde erfolgreich erstellt! Öffne 'animals.html' im Browser.")




