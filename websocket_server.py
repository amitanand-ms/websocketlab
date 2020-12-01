#!/usr/bin/env python3

import asyncio
import websockets

async def server(websocket, path):
    # Get received data from websocket

    i = 0

    while (i <= 0):

        data = await websocket.recv()

    # Send response back to client to acknowledge receiving message
        await websocket.send("Thanks for your message: " + data)
        mess=data.split(':')
        data=mess[1].split('"')
        print(data[1])
        if "bye" in data:
            print(data[1])
            i = 1

# Create websocket server
start_server = websockets.serve(server, "localserver",8080)

# Start and run websocket server forever
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
