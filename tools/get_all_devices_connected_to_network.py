import scapy.all as scapy
import re

# Regular expression pattern to recognize IPv4 addresses
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# get the address range to ARP
while True:
    ip_add_range_entered = "192.168.56.1/24"
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range")
        break

# trying ARPinng the ip address range supplied
arp_result = scapy.arping(ip_add_range_entered)
print(arp_result)