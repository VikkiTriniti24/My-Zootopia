import json

with open("animals_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)


output = ''  # Leerer String für die Tierdaten

for animal_data in data:
    output += '<li class="cards__item">\n'
    output += f"    Name: {animal_data['name']}<br/>\n"
    output += f"    Diet: {animal_data['characteristics'].get('diet', 'Unknown')}<br/>\n"
    output += f"    Location: {animal_data.get('locations', ['Unknown'])[0]}<br/>\n"
    output += f"    Type: {animal_data['characteristics'].get('type', 'Unknown')}<br/>\n"
    output += '</li>\n'

print(output)

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print("\n 'animals.html' wurde erfolgreich erstellt! Öffne die Datei im Browser.")

