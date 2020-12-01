#!/usr/bin/env python3

import asyncio
import websockets
import json
import urllib
import time


async def client():
    ip = input("Enter IP address for WS Server: ")
    uri = "ws://{0}:8080".format(ip)
    print(uri)
    async with websockets.connect(uri) as websocket:
        # Allow user to enter username into command line
        username = "Starting websocket with server {0}".format(ip)
        data = json.dumps({"username": username})

        # Send username as JSON object to server
        await websocket.send(data)
        
        response = await websocket.recv()
        print(response)

        i = 0
        y = 1

        while (i <= 0):

            message =  "Sending message{0}".format(y)
            data = json.dumps({"message" : message})

            await websocket.send(data)
            response = await websocket.recv()
            print(response)
            time.sleep(10)
            y = y+1

         #   if message == "bye":
          #      i = 1
        
asyncio.get_event_loop().run_until_complete(client())
