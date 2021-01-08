#!/bin/bash
sudo yum install python3 -y
sudo pip3 install asyncio
sudo pip3 install websockets
sudo cp ./client.py /home/testadmin/client.py
sudo chmod +x /home/testadmin/client.py
