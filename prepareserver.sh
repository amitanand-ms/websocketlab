#!/bin/bash
sudo yum install python3 -y
sudo pip3 install asyncio
sudo pip3 install websockets
sudo echo "10.1.1.10 localserver" >> /etc/hosts
sudo chmod +x ./websocketlab-main/websocket_server.py
./websocketlab-main/websocket_server.py &

