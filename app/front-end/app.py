#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    starters = ["bulbasaur", "charmander", "squirtle"]
    stats = {}
    for starter in starters:
        base_stat = requests.get(f"pokestats.default.svc.cluster.local:5000/stats/{starter}").json()
        stats[starter] = base_stat

    bulbasaur_stats = stats["bulbasaur"]
    charmander_stats = stats["charmander"]
    squirtle_stats = stats["squirtle"]

    if int(bulbasaur_stats) > int(charmander_stats) and int(bulbasaur_stats) > int(squirtle_stats):
        best_pokemon_starter = "bulbasaur"
    if int(charmander_stats) > int(bulbasaur_stats) and int(charmander_stats) > int(squirtle_stats):
        best_pokemon_starter = "charmander"
    if int(squirtle_stats) > int(bulbasaur_stats) and int(squirtle_stats) > int(charmander_stats):
        best_pokemon_starter = "squirtle"

    stats["best starter"] = best_pokemon_starter

    print(f"{stats=}")
    return render_template('home.html', stats=stats)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80)
