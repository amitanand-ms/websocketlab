#!/bin/bash
sudo yum install python3 -y
sudo pip3 install asyncio
sudo pip3 install websockets
sudo echo "10.1.1.10 localserver" >> /etc/hosts
cp ./websocket_server.py /home/testadmin
sudo chmod +x /home/testadmin/websocket_server.py
/home/testadmin/websocket_server.py &

