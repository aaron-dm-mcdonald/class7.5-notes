# Global ALB Load Testing & Guide

This document contains the Locust script for testing GCP Global Load Balancer regional spillover, installation instructions, and comparisons with other tools.

---

## What is Locust?
Locust is an open-source load testing tool where you define user behavior in Python. It is ideal for testing Global Load Balancers (ALBs) because it can scale to thousands of users to trigger regional overflow logic. In general its very easy to use because it can use the python ecosystem. 

### More background
From the [docs](https://github.com/locustio/locust):

"Locust tests can be run from command line or using its web-based UI. Throughput, response times and errors can be viewed in real time and/or exported for later analysis.

You can import regular Python libraries into your tests, and with Locust's pluggable architecture it is infinitely expandable. Unlike when using most other tools, your test design will never be limited by a GUI or domain-specific language."


### How the Code Works
* **HttpUser Class:** A template for a simulated user where each user is an independent object.
* **on_start:** Initializes tracking variables for each user.
* **@task:** The repeated action, which in this case is fetching JSON metadata.
* **Shift Logic:** The script only prints a message when the region returned by the LB changes for that specific user.

## How-To Guide: Locust Load Testing

### Installation

#### macOS
* **Via Homebrew:** `brew install locust`
* **Via Pip:** `pip3 install locust`

#### Windows
* **Via Chocolatey:** `choco install locust`
* **Via Pip:** `pip install locust`

### Running the Test

Start a test with this command:

```bash
locust -f locustfile.py --headless -u 100 -r 10 --host http://<LB_IP_ADDRESS>
```

### Flag Breakdown 
* `--headless`: Runs the test in the terminal without the web UI.
* `-u 100`: **Users**. Total concurrent users to simulate.
* `-r 10`: **Ramp-up**. Users spawned per second until reaching the limit.
* `--host`: The IP or URL of your Load Balancer.
* `-f`: Points to your script. Optional if your file is named `locustfile.py` in the current folder.

---

## Alternative Tools

### k6
A Go-based tool using JavaScript for scripting. It is highly resource-efficient and great for high-throughput testing and CI/CD integration.

### Apache JMeter
A Java-based industry standard with a GUI. It is more "heavyweight" but supports many protocols like FTP and JDBC, and offers better reporting.

---

