import os
from setuptools import setup, find_packages

def list_mathjax_files():
    # When dropping Python 2 support, this function
    # can be replaced with glob.iglob(..., recursive=True)
    files = []
    for root, _, filenames in os.walk('webviz/resources/js/mathjax'):
        dirname = root.replace('webviz/', '')  # relative to __init__.py
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
    return files

setup(
    name='webviz',
    version='0.10.0',
    packages=find_packages(exclude=['tests']),
    package_dir={"": "."},
    package_data={
        'webviz': ['templates/*',
                   'minimal_theme/templates/*',
                   'resources/css/*']
                  + list_mathjax_files()
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
