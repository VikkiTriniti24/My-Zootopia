import json

with open("animals_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

output = ''  # Leerer String für die Tierdaten

for animal_data in data:
    name = animal_data.get("name", "Unknown")
    diet = animal_data.get("characteristics", {}).get("diet", "Unknown")
    location = ", ".join(animal_data.get("locations", ["Unknown"]))  # Alle Locations als String
    type_ = animal_data.get("characteristics", {}).get("type", "Unknown")

    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    output += f'      <strong>Location:</strong> {location}<br/>\n'
    output += f'      <strong>Type:</strong> {type_}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'

print(output)  # Testausgabe

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print("\n 'animals.html' wurde erfolgreich erstellt! Öffne die Datei im Browser.")

