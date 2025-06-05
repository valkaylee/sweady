import threading
import uuid

from flask import Flask, jsonify, render_template, request

import pandas as pd
import measure
import classifier

app = Flask(__name__)

# In‐memory job store
# job format: { status: "pending"|"done", result: [...], user: "kaylee"|"jason" }
jobs = {}


def run_job(job_id, is_kaylee):
    measure.measure()

    clf = classifier.classify(is_kaylee)

    new_df = pd.read_csv("gsr_data.csv")
    new_df["predicted_state"] = clf.predict(new_df[["GSR"]])

    # compute the most common predicted state
    most_common = new_df["predicted_state"].mode()[0]

    jobs[job_id]["result"] = most_common
    jobs[job_id]["status"] = "done"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start_reading", methods=["POST"])
def start_reading():
    data = request.get_json() or {}
    user = data.get("user")
    if user not in ("kaylee", "jason"):
        return jsonify({"error": "invalid user"}), 400

    is_kaylee = (user == "kaylee")

    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "pending", "result": None, "user": user}

    thread = threading.Thread(target=run_job, args=(job_id, is_kaylee))
    thread.start()

    return jsonify({"job_id": job_id}), 202


@app.route("/result/<job_id>")
def get_result(job_id):
    job = jobs.get(job_id)
    if job is None:
        return jsonify({"error": "invalid job id"}), 404
    if job["status"] == "pending":
        return jsonify({"status": "pending"}), 202

    return jsonify({
        "status": "done",
        "state": job["result"]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
