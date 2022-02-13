#!/bin/bash

log=/home/noxyproxy/RandomCTF/htb_2021/boxes/ScriptKiddie/hackers

#cd /home/pwn/
cat $log | cut -d' ' -f3- | sort -u | while read ip; do
    echo "this si ip: $ip"
    sh -c "nmap --top-ports 10 -oN recon/${ip}.nmap ${ip} 2>&1 >/dev/null" &
done

if [[ $(wc -l < $log) -gt 0 ]]; then echo -n > $log; fi