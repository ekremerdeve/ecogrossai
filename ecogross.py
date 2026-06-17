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

app.run(debug=True)