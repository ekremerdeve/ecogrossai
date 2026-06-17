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

    if response.status_code != 200:
        return jsonify({"hata":"Migros sunucusuna erişilemedi"})

    try:
        data = response.json()
    except:
        return jsonify({
            "hata":"JSON okunamadı",
            "cevap": response.text[:500]
    })

    products = data["data"]["searchInfo"]["storeProductInfos"]

    sonuc = []

    for p in products[:10]:
        sonuc.append({
            "isim": p["name"],
            "fiyat": p["shownPrice"]/100
        })

    return jsonify(sonuc)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
