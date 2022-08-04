import argparse

HELP = 'Search for CTF related information, such as challenges, tips, etc.'
COMMAND = 'search'

def run(args: argparse.Namespace) -> None:
    print(args)

def init(parser: argparse.ArgumentParser) -> None:
    parser.set_defaults(func=run)