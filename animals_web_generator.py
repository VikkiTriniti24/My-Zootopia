import json

with open("animals_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

output = ""
for animal_data in data:
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics'].get('diet', 'Unknown')}\n"
    output += f"Location: {animal_data.get('locations', ['Unknown'])[0]}\n"
    output += f"Type: {animal_data['characteristics'].get('type', 'Unknown')}\n\n"

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print("Generiertes HTML:\n")
print(html_output)

print("\n 'animals.html' wurde erfolgreich erstellt! Öffne die Datei im Browser.")
