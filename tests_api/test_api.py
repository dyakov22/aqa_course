from backend import schemas
from backend.pets_interface import pet_api
from backend.schema_validation import validate_schema


def test_add_new_pet(generate_random_pet_id, clean_up_pet):
    payload = {
        "id": generate_random_pet_id,
        "category": {
            "id": 2,
            "name": "test"
        },
        "name": "bobby",
        "photoUrls": [
            "https://www.foof.com"
        ],
        "tags": [
            {
                "id": 10,
                "name": "ten"
            }
        ],
        "status": "not available"
    }
    response = pet_api.create_pet(payload=payload)
    assert response.status_code == 200
    validate_schema(response.json(), schemas.ADD_PET)


def test_delete_pet(create_pet):
    response = pet_api.delete_pet(pet_id=create_pet['id'])
    assert response.status_code == 200
    validate_schema(response.json(), schemas.DELETE_PET)


def test_find_pet_by_id(create_pet, clean_up_pet):
    response = pet_api.find_pet_by_id(pet_id=create_pet['id'])
    assert response.status_code == 200


def test_find_pet_by_alphabet():
    response = pet_api.find_pet_by_id(pet_id='p', negative_flow=True)
    print(response.json())
    assert response.status_code == 404

















