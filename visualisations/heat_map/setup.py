from setuptools import setup, find_packages

setup(
    name='webviz_heat_map',
    version='0.1.0',
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={
        'webviz_heat_map': []},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz', 'webviz_plotly', 'pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'heat_map = webviz_heat_map:HeatMap'
        ]
    },
    zip_safe=False
)
