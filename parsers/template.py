import argparse
import os

HELP = 'Template scripts for CTF competitions.'
COMMAND = 'template'


def run(args: argparse.Namespace) -> None:
    base_file = os.path.abspath(
        os.path.join(__file__, '..', '..', 'templates', args.category, args.template + '.py'))

    file_content = open(base_file, 'r').read()

    print(file_content)


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