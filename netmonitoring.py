import threading
import time
import os
import csv
from collections import Counter
from datetime import datetime

import matplotlib.pyplot as plt
from scapy.all import sniff, IP

# -----------------------------
# Global variables
# -----------------------------
traffic_counter = Counter()
lock = threading.Lock()

# Create logs directory
if not os.path.exists("logs"):
    os.makedirs("logs")


# -----------------------------
# Packet processing
# -----------------------------
def process_packet(packet):
    """Process each captured packet and update counters/logs."""
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

        # Update counter safely
        with lock:
            traffic_counter[src] += 1

        # Log packet
        with open("logs/packets.log", "a") as f:
            f.write(f"{datetime.now()}, {src} -> {dst}\n")


def capture_packets():
    """Capture packets continuously."""
    sniff(prn=process_packet, store=False)


# -----------------------------
# CSV logging
# -----------------------------
def save_top_talkers():
    """Save top talkers to CSV every 10 seconds."""
    while True:
        time.sleep(10)
        with lock:
            data = traffic_counter.most_common(10)

        if data:
            with open("logs/top_talkers.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Source IP", "Packet Count"])
                writer.writerows(data)

            print("[LOG] Top talkers saved to logs/top_talkers.csv")


# -----------------------------
# Live plotting
# -----------------------------
def live_plot():
    """Display a live graph of top talkers."""
    plt.ion()  # interactive mode ON
    fig, ax = plt.subplots()

    while True:
        time.sleep(3)  # update every 3 seconds
        with lock:
            data = traffic_counter.most_common(5)

        if data:
            sources, counts = zip(*data)
            ax.clear()
            ax.bar(sources, counts, color="skyblue")
            ax.set_title("Top Talkers (Live)")
            ax.set_xlabel("Source IP")
            ax.set_ylabel("Packet Count")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.draw()
            plt.pause(0.01)


# -----------------------------
# Main function
# -----------------------------
def main():
    print("🚀 Starting Network Monitor...")
    print("⚠️ Run as Administrator for best results.")
    print("📡 Capturing packets... Close graph window or press Ctrl+C to stop.")

    # Thread 1: Packet capture
    t1 = threading.Thread(target=capture_packets, daemon=True)
    t1.start()

    # Thread 2: CSV logging
    t2 = threading.Thread(target=save_top_talkers, daemon=True)
    t2.start()

    # Main thread: live plotting
    live_plot()


if __name__ == "__main__":
    main()
