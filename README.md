# 🐳 Dockerized Offline Data Generator

This is a **Docker-based automation project** developed as part of my DevOps learning journey. It is a Python application that runs inside a container, simulating real-time user activity logs without requiring an internet connection.

This project demonstrates the core concepts of **Containerization**, **Dockerfiles**, and **Image Management**.

---

## 🚀 Features
* **Fully Containerized:** Runs identically on any machine (Windows/Linux/Mac) using Docker.
* **Offline Simulation:** Generates mock user data (Logins, Purchases, Uploads) automatically.
* **Lightweight:** Built on top of the `python:3.9-slim` image for efficiency.
* **Automation:** Runs continuously in the background or foreground.

---


⚙️ How to Run
1. Build the Docker Image
Open your terminal in the project directory and run:

Bash
docker build -t offline-bot:v1 .
2. Run the Container
To start the bot and see the logs in real-time:

Bash
docker run --name my-bot offline-bot:v1
3. Run in Background (Detached Mode)
To let the automation run silently in the background:

Bash
docker run -d --name silent-bot offline-bot:v1
4. Check Logs (For Background Mode)
If running in background mode, use this to see the output:

Bash
docker logs -f silent-bot
5. Stop and Remove
To clean up the container:

Bash
docker rm -f my-bot silent-bot
🧠 What I Learned
By building this project, I practiced the following DevOps skills:

Writing Dockerfiles: Using FROM, WORKDIR, COPY, and CMD.

Building Images: converting code into a portable Docker image.

Container Lifecycle: Starting, stopping, and removing containers.

Troubleshooting: Debugging Docker build contexts and detached mode logs.
