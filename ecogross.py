from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/ara/<kelime>")
def ara(kelime):

    url = f"https://www.migros.com.tr/rest/search/screens/products?q={kelime}"

    headers = {
        "User-Agent":"Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    products = data["data"]["searchInfo"]["storeProductInfos"]

    sonuc = []

    for p in products[:10]:
        sonuc.append({
            "isim": p["name"],
            "fiyat": p["shownPrice"]/100
        })

    return jsonify(sonuc)

import os

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
