#!/usr/bin/env python

from glob import glob
from os import path, chdir, getcwd
from shutil import copytree, rmtree

from jinja2 import FileSystemLoader
from nbconvert import HTMLExporter
from nbconvert.writers import FilesWriter
from traitlets.config import Config
import nbformat
from datetime import datetime

IN_DIRECTORY = 'source'
OUT_DIRECTORY = 'public'
STYLES_DIRECTORY = 'css'
TEMPLATE_FILE = 'post.tpl'


class Chdir:
    def __init__(self, new_dir):
        self.new_dir = new_dir

    def __enter__(self):
        self.old_dir = getcwd()
        chdir(self.new_dir)

    def __exit__(self, *_args):
        chdir(self.old_dir)


def copy_files():
    rmtree(OUT_DIRECTORY, ignore_errors=True)
    copytree(IN_DIRECTORY, OUT_DIRECTORY)


def convert_notebooks():
    c = Config()
    c.HTMLExporter.preprocessors = [
        'nbconvert.preprocessors.ExtractOutputPreprocessor'
    ]

    html_exporter = HTMLExporter(
        config=c, extra_loaders=[FileSystemLoader(getcwd())])
    html_exporter.template_file = TEMPLATE_FILE

    writer = FilesWriter()

    with Chdir(OUT_DIRECTORY):
        glob_pattern = path.join('**', '*.ipynb')
        glob_results = glob(glob_pattern, recursive=True)

    for notebook_file in glob_results:
        out_path = path.dirname(notebook_file)
        full_out_path = path.join(OUT_DIRECTORY, out_path)

        with Chdir(full_out_path):
            print('Converting {}'.format(notebook_file))

            nb = nbformat.read(path.basename(
                notebook_file), nbformat.NO_CONVERT)
            nb['metadata']['human_date'] = datetime.strptime(
                nb['metadata']['date'], '%Y-%m-%d').strftime('%B %-d, %Y')
            nb['metadata']['path'] = out_path
            nb['metadata']['notebook_path'] = f'/{notebook_file}'
            nb['metadata'][
                'colab_url'] = f'https://colab.research.google.com/github/paulgb/notebooks/blob/master/{IN_DIRECTORY}/{notebook_file}'
            nb['metadata'][
                'binder_url'] = f'https://mybinder.org/v2/gh/paulgb/notebooks/master?filepath={IN_DIRECTORY}/{notebook_file}'

            (body, resources) = html_exporter.from_notebook_node(nb)
            writer.write(body, resources, notebook_name='index')


def copy_styles():
    with open(path.join(OUT_DIRECTORY, 'style.css'), 'w') as fh:
        for fname in sorted(glob(path.join(STYLES_DIRECTORY, '*.css'))):
            fh.write(open(fname).read())


def main():
    copy_files()
    convert_notebooks()
    copy_styles()


if __name__ == '__main__':
    main()
