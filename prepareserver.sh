#!/bin/bash
sudo yum install python3 -y
sudo pip3 install asyncio
sudo pip3 install websockets
sudo echo "10.1.1.10 localserver" >> /etc/hosts
sudo cp ./websocket_server.py /home/testadmin/websocket_server.py
sudo chmod +x /home/testadmin/websocket_server.py
sudo /home/testadmin/websocket_server.py &

