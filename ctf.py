#!/usr/bin/env python3
import argparse
import parsers.download
import parsers.template
import parsers.search


def add_subparsers(parser: argparse.ArgumentParser) -> None:
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    download_parser = subparsers.add_parser(parsers.download.COMMAND, help=parsers.download.HELP)
    parsers.download.init(download_parser)

    search_parser = subparsers.add_parser(parsers.search.COMMAND, help=parsers.search.HELP)
    parsers.search.init(search_parser)

    template_parser = subparsers.add_parser(parsers.template.COMMAND, help=parsers.template.HELP)
    parsers.template.init(template_parser)


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Utility script for CTF competitions.')
    add_subparsers(parser)
    args = parser.parse_args()

    args.func(args)


if __name__ == "__main__":
    main()