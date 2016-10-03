#!/bin/bash

script=example.py
username=jing
ip=192.168.33.10

ssh-keygen -f ~/.ssh/known_hosts -R $ip
sshpass -p 1234 scp -o StrictHostKeyChecking=no ./$script $username@$ip:/home/$username
sshpass -p 1234 ssh -X -o StrictHostKeyChecking=no -t $username@$ip "python $script"
