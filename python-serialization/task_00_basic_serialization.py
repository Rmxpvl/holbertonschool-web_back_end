#!/usr/bin/env python3
"""Basic serialization module"""

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "wb", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "rb", encoding="utf-8") as file:
        return json.load(file)