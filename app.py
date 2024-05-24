from flask import Flask, render_template, request, jsonify
from essaie import distribute_belts  # Importer la fonction de distribution

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_distribution", methods=["POST"])
def generate_distribution():
    belts = [
        int(request.form["beltGT"]),
        int(request.form["belt125"]),
        int(request.form["belt120"]),
        int(request.form["belt115"]),
        int(request.form["belt110"]),
        int(request.form["belt105"]),
        int(request.form["belt100"])
    ]
    distribution = distribute_belts(belts)
    return jsonify(distribution)

if __name__ == "__main__":
    app.run(debug=True)
