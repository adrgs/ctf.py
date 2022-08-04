import argparse
import os

HELP = 'Template scripts for CTF competitions.'
COMMAND = 'template'


def run(args: argparse.Namespace) -> None:
    bash_path = os.path.abspath(
        os.path.join(__file__, '..', '..', 'templates', args.category))

    for file in os.listdir(bash_path):
        if file.startswith(args.template+'.'):
            with open(os.path.join(bash_path, file), 'r') as f:
                print(f.read())


def init(parser: argparse.ArgumentParser) -> None:
    parser.set_defaults(func=run)

    template_folder = os.path.abspath(
        os.path.join(__file__, '..', '..', 'templates'))

    category = parser.add_subparsers(dest="category")
    category.required = True

    for category_name in os.listdir(template_folder):
        subparser = category.add_parser(
            category_name, help=f"Template for {category_name} category")

        template = subparser.add_subparsers(dest="template")
        template.required = True

        for template_name in os.listdir(
                os.path.join(template_folder, category_name)):
            template.add_parser(template_name[:template_name.find('.')],
                                help=f"{template_name} template")