from setuptools import setup, find_packages

setup(
    name='webviz',
    version='0.10.0',
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={
        'webviz': [
            'templates/*',
            'minimal_theme/templates/*',
            'resources/css/*',
            'resources/js/*'
        ]},
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
