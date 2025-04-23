from pydantic import TypeAdapter
from pydantic import HttpUrl

def check_str_is_http(x: str) -> str:
    http_url_adapter = TypeAdapter(HttpUrl)
    return str(http_url_adapter.validate_python(x))

print(check_str_is_http("nihao"))