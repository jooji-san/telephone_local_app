import sys
sys.path.append('../telephone_local_app')
from flask import Flask, render_template, request
from local import get_config_json, write_config_json, turn_off_AP, connect_wifi
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/wifi', methods=["POST"])
def wifi():
    config = get_config_json()
    ssid = request.form.get('ssid')
    password = request.form.get('password')
    config["wifi-networks"][ssid] = password
    write_config_json(config)



@app.route('/login', methods=["POST"])
def login():
    config = get_config_json(isAuth=True)
    email = request.form.get('email')
    password = request.form.get('password')
    config["email"] = email
    config["password"] = password
    write_config_json(config, isAuth=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8123)

@app.route('/finish')
def finish():
    turn_off_AP()
    connect_wifi()

