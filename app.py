from flask import Flask, jsonify
import wikipedia

app = Flask(__name__)

@app.route("/api/v1/search=<search>&lang=<lang>", methods=['GET'])
def home(search, lang):
        wikipedia.set_lang(f"{lang}")
        result = wikipedia.summary(search, sentences = 4)
        return jsonify({ "data": result })

if __name__ == "__main__":
    app.run()        