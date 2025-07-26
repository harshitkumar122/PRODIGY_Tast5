from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = packet.proto
        
        print(f"\n[+] Packet Captured:")
        print(f"    Source IP      : {src_ip}")
        print(f"    Destination IP : {dst_ip}")
        if TCP in packet:
            print("    Protocol       : TCP")
        elif UDP in packet:
            print("    Protocol       : UDP")
        else:
            print("    Protocol       : Other")
        print(f"    Payload        : {bytes(packet[IP].payload)[:50]}...")

print("Starting Packet Sniffer... (Press Ctrl+C to stop)\n")
sniff(prn=packet_callback, count=10)  
