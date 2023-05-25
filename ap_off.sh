#!/bin/bash
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
sudo systemctl stop nginx
sudo cp /etc/dhcpcd.conf.orig /etc/dhcpcd.conf
sudo systemctl daemon-reload
sudo systemctl restart dhcpcd
