from flask import Flask, request, jsonify, send_from_directory
from backend import retrieve_reports 
import os
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)  # ✅ 允许跨域请求

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index5.html")


@app.route("/api/upload", methods=["POST"])
def upload_image():
    image = request.files["image"]
    upload_dir = os.path.join(app.static_folder, "uploaded")
    os.makedirs(upload_dir, exist_ok=True) 
    image_path = os.path.join(upload_dir, image.filename)
    image.save(image_path)

    reports = retrieve_reports(image_path, topk=2)

    # 只提取文本
    report_texts = [r["text"] for r in reports]
    summary = "\n\n".join(report_texts)

    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
