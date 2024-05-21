import requests

import config

from jsonschema import validate
from backend import schemas

# from genson import SchemaBuilder
# builder = SchemaBuilder()
# builder.add_object(get_pets.json())

get_pets = requests.get(url=config.api.url + "pet/100")


validate(get_pets.json(), schemas.GET_PETS_SCHEMA)
