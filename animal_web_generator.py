import json


def load_data(file_path):
    """
    Load JSON data from a file.

    Args: file_path (str): The path to the JSON file containing animal data.

    Returns: list: A list of dictionaries, where each dictionary represents an animal and its data.
    """
    with open(file_path, "r") as file:
        return json.load(file)


def get_animals_info():
    """
    Generate formatted animal information as plain text.

    Returns: str: A string containing formatted information about each animal.
    """
    animals_data = load_data("animals_data.json")
    animal_info_html = "" # define an empty string

    for animal in animals_data:
        animal_name = animal["name"]
        animal_diet = animal["characteristics"]["diet"]
        animal_location = animal["locations"][0]
        # Use "Unknown" if the type is missing
        animal_type = animal["characteristics"].get("type", "Unknown")

        animal_info_html += (
            f"\n\t<li class='cards__item'>"
            f"\n\t\t<div class='card__title'>{animal_name}</div>\n"
            f"\t\t<p class='card__text'>\n"
            f"\t\t\t<ul>\n"
            f"\t\t\t\t<li><strong>Diet:</strong> {animal_diet}</li>\n"
            f"\t\t\t\t<li><strong>Location:</strong> {animal_location}</li>\n"
            f"\t\t\t\t<li><strong>Type:</strong> {animal_type}</li>\n"
            f"\t\t\t</ul>\n"
            f"\t\t</p>\n"
            f"\t</li>\n"
        )
    return animal_info_html


def make_new_html_file(file_path):
    """
    Create a new HTML file by replacing a placeholder in a template file
    with the generated animal information.

    Args: file_path (str): Path to the template HTML file.
    """
    with open(file_path, "r") as file:
        read_animals_info = file.read()

    old_content = "__REPLACE_ANIMALS_INFO__"
    new_content = get_animals_info()
    updated_html_content = (
        read_animals_info.replace(old_content, new_content))

    new_html = "animals.html"
    with open(new_html, "w") as file:
        file.write(updated_html_content)


def main():
    """
    Main function to execute the script. Reads a template file,
    generates animal information, and creates a new HTML file.
    """
    template_file = "animals_template.html"
    make_new_html_file(template_file)


if __name__ == "__main__":
    main()