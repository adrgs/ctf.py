#!/usr/bin/env python3

from pwn import *
import argparse


def main(args: argparse.Namespace) -> None:
    args.remote = '' or args.remote
    args.port = 0 or args.port
    args.file = '/bin/bash' or args.file
    args.libc = '' or args.libc

    context.clear(arch = 'amd64')

    if args.remote and args.port:
        sh = remote(args.remote, args.port)
    else:
        sh = process(args.file)

    # https://github.com/Gallopsled/pwntools-tutorial

    libc = ELF(args.libc)
    binary = ELF(args.file)

    rop = ROP(binary)
    payload = b''

    sh.sendline(payload)

    if args.debug:
        # context.terminal = ["tmux", "splitw", "-h"]
        gdb.attach(sh, '''
            break *0xADD2E55
        ''')

    sh.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Buffer overflow pwn script')
    parser.add_argument('-r', '--remote', help='Remote host')
    parser.add_argument('-p', '--port', type=int, help='Remote port')
    parser.add_argument('-f', '--file', help='Local file')
    parser.add_argument('-l',
                        '--libc',
                        help='Local libc',
                        default='/lib/x86_64-linux-gnu/libc.so.6')
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