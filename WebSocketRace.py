import asyncio
from csv import Error
from click import option
from uritemplate import variables
import websockets
import argparse

import Utility

import re

paraser = argparse.ArgumentParser(prog="WebsocketRace")

paraser.add_argument('-g', '--gate',type=str, help="First data to send", required=True)
paraser.add_argument('-r', '--run', help="Run Gate", action='store_true')

paraser.add_argument('-d1','--data_one', type=str, help="First data to send", default="")
paraser.add_argument('-d2', '--data_two', type=str, help="Second data to send", default="")

paraser.add_argument('-c', '--connection_message', type=str, help="Connection Message", default="")
paraser.add_argument('-v', '--variables', type=str, help="Space separated variables, format NAME:VALUE", default="")

paraser.add_argument('-b', '--cookies', type=str, help="Cookies", default="")
paraser.add_argument('-o', '--origin', type=str, help="Whitelisted Origin", default="")

paraser.add_argument('-u', '--url', type=str, help="Target URL for Websocket Connection", default="")

args = paraser.parse_args()

# Thread for sending request
async def send_request(options, data):
    async with websockets.connect(options.url, extra_headers={'Origin': options.origin, 'Cookie': options.cookies}) as websocket:
        if(options.connection_message != ""):
            await websocket.send(options.connection_message)

            response = await websocket.recv()

            print(f"Connection: {response}")

        await asyncio.sleep(2)

        await websocket.send(options.data)

        await asyncio.sleep(2)

        response = await websocket.recv()

        print(f"Response: {response}")

        await websocket.close()

# Lining up of the requests
async def main(options):
    await asyncio.gather(
        send_request(options, options.data_one),
        send_request(options, options.data_two)
    )

#Initialise Gate

if(not args.run):
    Utility.map_to_options(args.gate, args)
else:
    options = Utility.fetch_options(args.gate)

    variables = Utility.variables_to_dict(args.variables)

    for key in variables.keys():
        options.connection_message = options.connection_message.replace(key, variables[key])
        options.cookies = options.cookies.replace(key, variables[key])
        options.data_one = options.data_one.replace(key, variables[key])
        options.data_two = options.data_two.replace(key, variables[key])

    if(options.url == ""):
        raise SystemExit("Invalid URL")
    
    asyncio.run(main(options))