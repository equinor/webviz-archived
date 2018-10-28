import os
from setuptools import setup, find_packages

def list_mathjax_subdirs(mathjax_root, package_root):
    return [os.path.join(os.path.relpath(dirname, package_root), '*') for
            dirname, _, _ in os.walk(mathjax_root)]

setup(
    name='webviz',
    version='0.10.0',
    packages=find_packages(exclude=['tests']),
    package_dir={"": "."},
    package_data={
        'webviz': ['templates/*',
                   'minimal_theme/templates/*',
                   'resources/css/*']
                  + list_mathjax_subdirs('webviz/resources/js/mathjax',
                                         './webviz')
        },
    test_suite="setup.discover_test_suite",
    install_requires=[
        'jinja2',
        'markdown',
        'pygments',
        'six',
        'argparse',
        'ordered-set',
        'pyyaml',
        'future',
        'python-markdown-math'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle'],
    entry_points={
        'webviz_themes': [
            'minimal = webviz.minimal_theme:minimal_theme'
        ],
        'webviz_page_elements': [
            'Html = webviz:Html'
        ]
    },
    zip_safe=False
)
