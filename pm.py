#!/usr/bin/env python3
import json, toml
from flask import Flask, request, jsonify
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/wake', methods=['GET'])
def query_records():
    name = request.args.get('name')
    if name is None:
        return jsonify({'status': 'error', 'message': 'No name was provided!'})
    config = toml.load("config.toml")
    address = config["host"][name]["mac"]
    print(f"Waking up host {name} with address {address}")
    send_magic_packet(address)
    return jsonify({'status': 'success'})


if __name__ == "__main__":
    app.run(debug=True)
