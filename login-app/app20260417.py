from flask import Flask, request, jsonify, render_template

PREFIX = "/codeeditor/default/ports/5000"

app = Flask(__name__)

USERS = {
    "admin": "password123",
    "user": "pass",
}


@app.route("/codeeditor/default/ports/5000/")
@app.route("/codeeditor/default/ports/5000/login")
@app.route("/")
@app.route("/login")
def index():
    return render_template("login20260417.html", prefix=PREFIX)


@app.route("/codeeditor/default/ports/5000/auth", methods=["POST"])
@app.route("/auth", methods=["POST"])
def auth():
    data = request.get_json()
    uid = data.get("u", "")
    pwd = data.get("p", "")
    if uid in USERS and USERS[uid] == pwd:
        return jsonify({"ok": True, "name": uid})
    return jsonify({"ok": False}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
