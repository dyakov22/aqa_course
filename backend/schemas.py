

GET_PETS_SCHEMA = {
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "category": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name"
      ]
    },
    "name": {
      "type": "string"
    },
    "photoUrls": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "name"
        ]
      }
    },
    "status": {
      "type": "string"
    }
  },
  "required": [
    "category",
    "id",
    "name",
    "photoUrls",
    "status",
    "tags",
    "id1"
  ]
}
