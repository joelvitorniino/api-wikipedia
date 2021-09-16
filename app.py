from flask import Flask, jsonify
import wikipedia

app = Flask(__name__)

@app.route("/api/v1/search=<search>&lang=<lang>", methods=["POST", "GET"])
def home(search, lang):
    wikipedia.set_lang(f"{lang}")
    try:
       result = wikipedia.summary(search, sentences=4) 
       return jsonify({"data": result})
    except wikipedia.DisambiguationError:
        return jsonify({"data": "Pesquisa não encontrada, por favor tente com outro nome parecido." })  

if __name__ == "__main__":
    app.run()