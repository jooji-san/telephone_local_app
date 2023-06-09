import json
from subprocess import run
from urllib.request import urlopen


def connect_wifi():
    config = get_config_json()
    
    # add those in wpa_supplicant.conf (overwrite from third line)
    # take two lines from existing conf
    with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'r') as f:
        lines = f.readlines()

    del lines[2:]

    wifi_networks = config["wifi-networks"]
    print(wifi_networks)

    for ssid, password in wifi_networks.items():
        output = run(f'wpa_passphrase {ssid} {password}', check=True, shell=True)
        lines.append(output.decode('utf-8'))

    with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as f:
        f.writelines(lines)

    run('sudo rfkill unblock wifi', shell=True)
    run('sudo wpa_cli -i wlan0 reconfigure')
    
def get_config_json(isAuth=False):
    path = '../config.json'
    if isAuth:
        path = '../auth.json'

    with open(path, 'r') as f:
        json_lines = f.read()
        config = json.loads(json_lines)
        print(config)
        return config
    
def write_config_json(dic, isAuth=False):
    path = '../config.json'
    if isAuth:
        path = '../auth.json'

    with open(path, 'w') as f:
        configJSON = json.dumps(dic)
        f.write(configJSON)

def is_connected():
    try:
        urlopen('https://www.google.com/', timeout=10)
        return True
    except: 
        return False

def turn_on_AP():
    run('./ap_on.sh')

def turn_off_AP():
    run('./ap_off.sh')

