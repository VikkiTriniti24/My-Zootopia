import data_fetcher
import json


def serialize_animal(animal_obj):
    """Serializes a single animal as an HTML list item."""
    name = animal_obj.get("name", "Unknown")
    diet = animal_obj.get("characteristics", {}).get("diet", "Unknown")
    locations = animal_obj.get("locations", ["Unknown"])
    location = locations[0] if locations else "Unknown"  # Print only one location
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


def main():
    """Main function handling user input, data fetching, and HTML generation."""
    animal_name = input("Please enter an animal: ").strip()

    # Fetch data from API
    data = data_fetcher.fetch_data(animal_name)

    if not data:
        print(f"No data found for '{animal_name}'. Exiting program.")
        return

    # Serialize all animals
    output = ''.join(serialize_animal(animal) for animal in data)

    try:
        # Read HTML template
        with open("animals_template.html", "r", encoding="utf-8") as file:
            html_template = file.read()

        # Replace placeholder
        html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

        # Write the new HTML to a file
        with open("animals.html", "w", encoding="utf-8") as file:
            file.write(html_output)

        print(f"\nWebsite for '{animal_name}' was successfully created! Open 'animals.html' in your browser.")

    except FileNotFoundError:
        print("Error: Template file 'animals_template.html' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

