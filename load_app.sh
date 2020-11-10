#!/bin/bas

while true; do
    ab -n 50 -c 4 http://192.168.64.3:30800/user;
    sleep 3;
done
