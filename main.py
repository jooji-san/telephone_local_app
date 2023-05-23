import json

# read wifi credentials from config.json
with open('config.json', 'r') as f:
    json_lines = f.read()
    print(json_lines)
    config = json.loads(json_lines)

# add those in wpa_supplicant.conf (overwrite from third line)
# take two lines from existing conf
with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'r') as f:
    lines = f.readlines()

del lines[2:]

print(config[wifi-networks])

for ssid, password in wifi_networks.items():
    lines.push(check_output(f'wpa_passphrase {ssid} {password}'))

with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as f:
    f.writelines(lines)
