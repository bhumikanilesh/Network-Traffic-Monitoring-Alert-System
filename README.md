# Network-Traffic-Monitoring-Alert-System
This project tackles the challenge of monitoring and analyzing real-time network traffic, helping identify devices that consume excessive bandwidth and flagging suspicious activity. It captures live packets, tracks usage by IP addresses, and raises alerts when thresholds are exceeded, visualizes the top talkers with logs are stored for record. The system demonstrates applied knowledge of networking, automation, and data visualization in a practical tool.

 # Key Highlights
Problem Solved: Detects unusual network activity and monitors top bandwidth consumers in real-time.
Tools & Technologies: Python, Scapy, Matplotlib, Pandas, and Plyer for alerts.

# Features
* Real-time packet capture and analysis
* Live interactive graph of top network talkers
* CSV logs (top_talkers.csv & alerts.csv) for offline analysis
* Desktop notifications for high traffic alerts
* Works on both Windows (with Npcap) and Linux

# Installation
git clone https://github.com/bhumikanilesh/Network-Traffic-Monitoring-Alert-System/tree/main.git
cd network-monitoring-system
pip install -r requirements.txt

# Usage
Run with administrator/root privileges:
python netmonitoring.py


Logs will be saved in the logs/ folder, and a live interactive graph will display the top traffic-generating IPs.
