import argparse

HELP = 'Download files from popular CTF platforms like CTFd or CyberEDU.'
COMMAND = 'download'

def run(args: argparse.Namespace) -> None:
    print(args)

def init(parser: argparse.ArgumentParser) -> None:
    parser.set_defaults(func=run)