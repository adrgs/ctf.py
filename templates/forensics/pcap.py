#!/usr/bin/env python3
from scapy.layers.http import *
from scapy.all import *
from scapy.sessions import TCPSession
import argparse


def main(args: argparse.Namespace) -> None:
    scapy_cap = rdpcap('filtered.pcapng')
    for packet in scapy_cap:
        # do something with the packet
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Buffer overflow pwn script')
    parser.add_argument('-f', '--file', help='Local file')
    parser.add_argument('-d',
                        '--debug',
                        action='store_true',
                        help='Enable debug')
    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='Enable verbose')
    args = parser.parse_args()

    main(args)