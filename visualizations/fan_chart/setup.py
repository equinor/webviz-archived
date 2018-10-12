from setuptools import setup, find_packages

setup(
    name='webviz_fan_chart',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    package_dir={"": "."},
    package_data={
        'webviz_fan_chart': []},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz', 'webviz_plotly', 'pandas', 'matplotlib'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'FanChart = webviz_fan_chart:FanChart'
        ]
    },
    zip_safe=False
)
