#!/bin/bash
sudo cp /etc/dhcpcd.conf.new /etc/dhcpcd.conf
sudo systemctl daemon-reload
sudo systemctl restart dhcpcd
sudo systemctl start dnsmasq
sudo systemctl start hostapd
sudo systemctl start nginx
