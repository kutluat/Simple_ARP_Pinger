import argparse
import scapy.all as scapy

parser = argparse.ArgumentParser()

parser.add_argument('-i','--ipaddress',type=str,help="")

args = parser.parse_args()

ip_range = args.ipaddress

ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip_range), timeout=2)

ans.summary()