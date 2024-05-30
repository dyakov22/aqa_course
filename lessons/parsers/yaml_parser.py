import yaml


with open("../files_for_parsing/example.yaml", "r") as file:

    result = yaml.safe_load(file)

    print(result)