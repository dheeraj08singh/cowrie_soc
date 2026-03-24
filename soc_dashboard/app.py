from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# ✅ Updated path (JSON log file)
LOG_FILE = "/home/kali/Desktop/cowrie_soc/cowrie/var/log/cowrie/cowrie.json"

def read_logs():
    events = []
    alert = None

    if not os.path.exists(LOG_FILE):
        return alert, events

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    # Read last 10 logs
    for line in reversed(lines[-10:]):
        try:
            data = json.loads(line)

            timestamp = data.get("timestamp", "")
            src_ip = data.get("src_ip", "")
            eventid = data.get("eventid", "")

            event = f"[{timestamp}] {src_ip} → {eventid}"
            events.append(event)

            # Alert for successful login
            if eventid == "cowrie.login.success":
                alert = f"Successful login: {src_ip}"

        except:
            continue

    return alert, events


@app.route("/")
def index():
    alert, events = read_logs()
    return render_template("index.html", alert=alert, events=events)


if __name__ == "__main__":
    app.run(debug=True)
