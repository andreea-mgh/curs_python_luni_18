from flask import Flask, request, jsonify

app = Flask("server_cool")
prieteni = []

# GET  = clientul cere date de la server
# POST = clientul trimite date către server
@app.route("/salut", methods=["GET"])
def salut():
    return jsonify({"message":"Salut!"}), 200

@app.route("/prieten", methods=["GET", "POST"])
def prieten():
    if request.method == "POST":
        p = request.json
        prieteni.append(p)
        return jsonify({"message":"adaugat prieten"}), 201
    if request.method == "GET":
        id = request.args.get("id")
        if id is None:
            # daca nu scriu al catelea prieten vreau,
            # returneaza toti prietenii
            return jsonify(prieteni), 200
        id = int(id)
        if id >= len(prieteni):
            # daca cautam un prieten care nu exista
            # returneaza 404 (not found)
            return jsonify({"status":"error"}), 404
        return jsonify(prieteni[id])
        



# 404: Not Found
# 400: Bad Request

# 200: GET successful 
# 201: POST saved to server

app.run(host="0.0.0.0",port=5000)