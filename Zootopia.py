import json

def load_data(file_path):
    """Loads a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return []

def generate_animal_info(animals_data):
    """Generates an HTML formatted string with animal data."""
    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        if 'name' in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'
        if 'characteristics' in animal and isinstance(animal['characteristics'], dict):
            characteristics = animal['characteristics']
            if 'diet' in characteristics:
                output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
            if 'location' in characteristics:
                output += f'      <strong>Location:</strong> {characteristics["location"]}<br/>\n'
            if 'type' in characteristics:
                output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'
        output += '  </p>\n</li>\n'
    return output

def generate_html(template_path, output_path, animals_data):
    """Reads HTML template, replaces placeholder with animal data, and writes to output file."""
    try:
        with open(template_path, "r", encoding="utf-8") as template_file:
            html_content = template_file.read()
    except FileNotFoundError:
        print(f"Error: Template file {template_path} not found.")
        return
    
    animal_info = generate_animal_info(animals_data)
    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)
    
    try:
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(new_html_content)
    except IOError:
        print(f"Error: Unable to write to {output_path}.")

animals_data = load_data('animals_data.json')
if animals_data:
    generate_html('animals_template.html', 'animals.html', animals_data.json)
