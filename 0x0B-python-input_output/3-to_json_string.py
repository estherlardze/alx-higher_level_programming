#!/usr/bin/python3
""" Module: 3-to_json_string """

import json


def to_json_string(my_obj):
    """
        Return json representation of an object
        Args:
            obj- object to convert to json
    """

    return json.dumps(my_obj)
