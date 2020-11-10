#!/bin/bas

while true; do
    ab -n 10000 -c 200 http://arch.homework/otusapp/ksalov/user;
    sleep 1;
done
