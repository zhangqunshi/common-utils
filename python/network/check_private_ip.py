# coding: utf8

#
# check if the ips in a file is a private
# NOTE: the ip address should be first column in the file.
#

from IPy import IP  # you need "pip install ipy"

filename = "all_ips.txt" 

net_a = IP('10.0.0.0-10.255.255.255', make_net=True)
net_b = IP('172.16.0.0-172.31.255.255', make_net=True)
net_c = IP('192.168.0.0-192.168.255.255', make_net=True)

ipset = set()
with open(filename) as f:
    for x in f.readlines():
        ipaddr = x[0:15]
        ipaddr = ipaddr.strip()
        if (ipaddr not in net_a) and (ipaddr not in net_b) and (ipaddr not in net_c):
            print("IP address %s is not private" % ipaddr)
            continue
        if ipaddr.split(".")[3] == "255":
            print("broadcast ip: %s" % ipaddr)
            continue
        ipset.add(ipaddr)

print(ipset)
print("Total private ip count: %s" % len(ipset))
