# -*- coding: utf-8 -*-


USER_SCHEMA = {
    "username": {"type": "string", "required": True, },
    "firstName": {"type": "string", "rename": "first_name", },
    "lastName": {"type": "string", "rename": "last_name", },
    "email": {
        "type": "string",
        "required": True,
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"},
    "phone": {"type": "string", "required": True, },
}
