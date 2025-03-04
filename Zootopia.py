import json

def load_data(file_path):


    def print_animal_info(animals_data):

        for animal in animals_data:
            if "name" in animal:
                print(f"Name: {animal['name']}")
            if "diet" in animal:
                print(f"Diet: {animal['diet']}")
            if "locations" in animal and animal["locations"]:
                print(f"Location: {animal['locations'][0]}")
            if "type" in animal:
                print(f"Type: {animal['type']}")
            print()

animals_data = load_data('animals_data.json')


with open("animals_template.html", "r") as file:
    template_content = file.read()


animals = [
    {"name": "American Foxhound", "characteristics": {"diet": "Omnivore", "location": "North-America", "type": "Hound"}},
    {"name": "Arctic Fox", "characteristics": {"diet": "Carnivore", "location": "Eurasia", "type": "Mammal"}},

]


output = ""
for animal_data in animals:
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics']['diet']}\n"
    output += f"Location: {animal_data['characteristics']['location']}\n"
    output += f"Type: {animal_data['characteristics']['type']}\n\n"



updated_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as file:
    file.write(updated_html)

print("animals.html generated successfully! Open it in your browser to check.")
