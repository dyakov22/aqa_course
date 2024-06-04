from typing import Union

from genson import SchemaBuilder
from requests import Response


def schema_generation(response: Union[Response, dict]):
    sb = SchemaBuilder()

    if isinstance(response, Response):
        raw_schema = response.json()
    else:
        raw_schema = response

    sb.add_object(raw_schema)

    return sb.to_schema()
