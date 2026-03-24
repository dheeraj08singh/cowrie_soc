# 🛡️ Cowrie Honeypot SOC Dashboard Project

## 📌 Overview

This project demonstrates how a beginner in cybersecurity can build a **Security Operations Center (SOC) monitoring setup** using a honeypot and a custom dashboard.

The goal was to simulate real-world attack scenarios, capture attacker activity, and visualize logs for analysis — similar to what SOC analysts do in real environments.

## 🎯 Objectives

* Understand how honeypots work in cybersecurity
* Capture real-world attack attempts using Cowrie
* Analyze logs generated from attacker interactions
* Build a simple SOC dashboard for visualization
* Gain hands-on experience in log monitoring and detection

---

## 🧰 Tools & Technologies Used

* 🐍 Python (Flask)
* 📊 HTML (Dashboard UI)
* 🐧 Kali Linux
* 🍯 Cowrie (Honeypot for capturing attacks)

---

## 🏗️ Project Architecture

1. Cowrie honeypot is deployed on a system
2. Attackers (bots/scanners) attempt SSH/Telnet login
3. Cowrie logs all activities (IP, commands, login attempts)
4. Logs are processed and visualized using a custom SOC dashboard

---

## 📂 Project Structure

```
cowrie-honeypot-soc-lab/
 ├── soc_dashboard/
 │    ├── app.py
 │    └── templates/
 │         └── index.html
 ├── README.md
 └── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Cowrie

```
git clone https://github.com/cowrie/cowrie
cd cowrie
```

### 2️⃣ Run Cowrie

```
./bin/cowrie start
```

### 3️⃣ Generate Logs

* Let the honeypot run
* Wait for login attempts from bots/attackers

### 4️⃣ Run SOC Dashboard

```
cd soc_dashboard
python3 app.py
```

### 5️⃣ Access Dashboard

Open browser:

```
http://localhost:5000
```

---

## 🔍 What I Learned

* Basics of honeypots and how attackers interact with systems
* Log analysis and monitoring techniques
* Building a simple web-based dashboard using Flask
* Understanding real-world SOC workflows
* Handling Git and GitHub for project management

---

## 🚨 Sample Observations

* Multiple failed SSH login attempts
* Common usernames: `root`, `admin`, `test`
* Automated bot activity from different IP addresses
* Repeated brute-force patterns


## 🙋‍♂️ About Me

I am a beginner in cybersecurity transitioning into SOC/Cloud Security.
This project is part of my hands-on learning journey to gain practical experience.

---

## ⭐ Conclusion

This project helped me understand how SOC analysts monitor threats, analyze logs, and respond to suspicious activities in real-world environments.

---

## 📌 Note

Cowrie is an open-source honeypot and is not included in this repository.
Please follow the setup instructions to install and run it separately.


