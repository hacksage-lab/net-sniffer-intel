from scapy.all import sniff

def process_packet(packet):
    if packet.haslayer('IP'):
        ip_layer = packet['IP']
        print(f"[+] New Packet: {ip_layer.src} -> {ip_layer.dst}")
        print(f"    Protocol: {ip_layer.proto}")
        if packet.haslayer('TCP') or packet.haslayer('UDP'):
            print(f"    Ports: {packet.sport} -> {packet.dport}")
        print("-"*60)
    
sniff(filter="ip", prn=process_packet, store=0)