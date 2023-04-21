from flask import Flask, request, render_template
import json
import os
import uuid
import toml

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./uploads"

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():
    data = json.loads(request.data)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_id + ".toml")

    with open(file_path, "w") as f:
        toml.dump(data, f)

    return {"file_id": file_id}


@app.route("/download/<file_id>", methods=["GET"])
def download(file_id):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_id + ".toml")
    if os.path.exists(file_path):
        return send_from_directory(app.config["UPLOAD_FOLDER"], file_id + ".toml", as_attachment=True)
    else:
        return "File not found", 404


if __name__ == "__main__":
    app.run(debug=True)
