#! /usr/bin/env python
from past.builtins import raw_input
from scapy.all import *


def sniff_packets(packets):
    a = sniff(count=packets)
    a.nsummary()


print("\nCN5204 Final Project - Task 4")
print("* TO CLOSE THE APPLICATION ENTER THE LETTER Q")


while True:
    user_input = raw_input("\nEnter the number of packets that will be captured: ").lower().rstrip()

    if user_input:
        if user_input.lower() == "q":
            break
        else:
            print("\nRUNNING ... \n")
            sniff_packets(int(user_input))
            print("\n" + "*" * 60)

    else:
        print('\n\033[91m❎ Please enter the number of packets!\033[0m')
