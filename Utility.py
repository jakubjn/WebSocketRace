from ast import arg
import json

from dataclasses import dataclass, asdict
from typing import Dict

DATA_FILE = 'data.json'

@dataclass
class RequestOptions:
    connection_message: str = ""
    cookies: str = ""
    origin: str = ""
    data_one: str = ""
    data_two: str = ""
    url: str = ""

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d: dict):
        return RequestOptions(**d)
    
def fetch_options(gate_name):
    dict = json.loads(open(DATA_FILE).read())

    if(dict.get(gate_name)):
        return RequestOptions.from_dict(dict[gate_name])

    return RequestOptions()

def map_to_options(gate_name, args):
    options = fetch_options(gate_name)

    if args.connection_message != "":
        options.connection_message = args.connection_message
    if args.cookies != "":
        options.cookies = args.cookies
    if args.origin != "":
        options.origin = args.origin
    if args.data_one != "":
        options.data_one = args.data_one
    if args.data_two != "":
        options.data_two = args.data_two
    if args.url != "":
        options.url = args.url

    dict = json.loads(open(DATA_FILE).read())
    options_dict = options.to_dict()

    dict[gate_name] = options_dict

    with open(DATA_FILE, "w") as file:
        file.write(json.dumps(dict, indent=2))

