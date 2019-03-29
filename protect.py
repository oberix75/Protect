#!/usr/bin/python

import argparse,os

parser = argparse.ArgumentParser(description='Protect you with iptables (Linux) (root)')
parser.add_argument('-p', '--protect', dest='str', metavar="ddos,scan,spoof",
                help= """ Put [ddos] for protection anti-ddos,
                [scan] for protection anti-scan, [spoof] for protection anti-spoof""")
args = parser.parse_args()

str = args.str
    
if str == "ddos":
    os.system("sudo bash protect_1.sh")
elif str == "scan":
    os.system("sudo bash protect_2.sh")
elif str == "spoof":
    os.system("sudo bash protect_3.sh")
else:
    parser.print_help()
