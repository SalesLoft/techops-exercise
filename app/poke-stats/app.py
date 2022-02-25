#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import requests

app = Flask(__name__)

@app.route("/stats/<pokemon_name>")
def get_stats(pokemon_name):
    r = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_name))
    data = r.json()

    total_base_stat_points = 0
    for i in range(len(data["stats"])):
        total_base_stat_points = total_base_stat_points + data["stats"][i]["base_stat"]

    return str(total_base_stat_points)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
