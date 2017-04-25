#!/usr/bin/env python3

import ipaddress
import subprocess
import argparse
import socket


# To-DO:
#   Concurrency - create queue and add threads 
#   How to handle /32 "network"
#   DNS Lookup Hosts and write hostnames
#       socket.gethostbyaddr()
#   ?Hook into Database? - Save results (Different script?)
#   ?Another way to determine hostnames other than DNS?
#   ?Different imlementation of ping other than system call?
#       ICMP? UDP? Sockets? Scapy? How to determine success/failure?
#   More comments
#   Logging
#   How about if system is offline but provisioned? Notification lag?

def setup_args(argv=None):
    '''
    Function builds parsing object
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("subnet", help = "Input IPv4 subnet in CIDR notation")
    return parser


def run_shell_cmd(cmd, *shell):
    '''
    Function that allows Python to call a shell command.
    '''
    if "shell" in shell:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    else:
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    # output variable allows capability of printing stdout but also causes
    # the script to wait for the subprocess to finish before proceeding.
    output = process.communicate()[0]
    rcode = process.returncode
    return output, rcode


def main():
    '''
    The script's main function
    '''

    p = setup_args()
    args = p.parse_args()
    subnet = args.subnet
    ip_network = ipaddress.ip_network(subnet)
    all_ips= list(ip_network.hosts())

    print("The subnet", subnet, "has", len(all_ips), "usable IP addresses:")
    print("Start:", all_ips[0])
    print("End:", all_ips[-1])
    print()


    for i in range(len(all_ips)):
        ip = str(all_ips[i])
        output, returncode = run_shell_cmd("ping -c 3 -W 500 " + ip)
        if returncode is 0:
            print(ip, "is online.")
        else:
            print(ip, "is offline.")



if __name__ == "__main__":
    main()
