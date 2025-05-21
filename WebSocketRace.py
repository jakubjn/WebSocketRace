import asyncio
import websockets
import argparse

paraser = argparse.ArgumentParser(prog="WebsocketRace")

paraser.add_argument('-d1','--data_one', type=str, help="First data to send", required=True)
paraser.add_argument('-d2', '--data_two', type=str, help="Second data to send")

paraser.add_argument('-c', '--connection', type=str, help="First Connection Message", default="")

paraser.add_argument('--cookie', type=str, help="Cookies", default="")
paraser.add_argument('--origin', type=str, help="Whitelisted Origin", default="")

paraser.add_argument('-u', '--url', type=str, help="Target URL for Websocket Connection", required=True)

args = paraser.parse_args()

async def send_request(uri, message, connection_message):
    async with websockets.connect(uri, extra_headers={'Origin': args.origin, 'Cookie': args.cookie}) as websocket:
        if(connection_message != ""):
            await websocket.send(connection_message)

            response = await websocket.recv()

            print(f"Connection: {response}")

        await asyncio.sleep(2)

        await websocket.send(message)

        await asyncio.sleep(2)

        response = await websocket.recv()

        print(f"Message: {message}")
        print(f"Response: {response}")

        await websocket.close()

async def main():
    await asyncio.gather(
        send_request(args.url, args.data_one, args.connection),
        send_request(args.url, args.data_two, args.connection)
    )

if __name__ == "__main__":
    asyncio.run(main())