# 🧠 Network Packet Analyzer | Task-05

This is a simple **Network Packet Sniffer** built using Python and the Scapy library. Developed as part of the **Cybersecurity Internship** at **Prodigy InfoTech**, it demonstrates how to capture and analyze packets for learning and research purposes.

## 📌 Features

- Captures live network packets
- Extracts and displays:
  - Source IP address
  - Destination IP address
  - Protocol (TCP/UDP)
  - Payload (first 50 bytes)
- Designed for **educational** and **ethical** use only

## 🛠️ Tech Stack

- Python 3.x
- [Scapy](https://scapy.net/)
- OS: Windows/Linux

## ⚙️ Setup & Run

### 🔧 Installation

Make sure Python is installed. Then, install Scapy:
bash
pip install scapy

📋 Sample Output
[+] Packet Captured:
    Source IP      : 192.168.1.5
    Destination IP : 93.184.216.34
    Protocol       : TCP
    Payload        : b'GET / HTTP/1.1\r\nHost: example.com\r\n...' 
