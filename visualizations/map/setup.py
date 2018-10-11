from setuptools import setup, find_packages

setup(
    name='webviz_map',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    package_dir={"": "."},
    package_data={
        'webviz_map': [
            'templates/*',
            'resources/js/*'
        ]},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'Map = webviz_map:Map',
        ]
    },
    zip_safe=False
)
