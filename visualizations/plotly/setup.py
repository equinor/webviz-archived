from setuptools import setup, find_packages

setup(
    name='webviz_plotly',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    package_dir={"": "."},
    package_data={
        'webviz_plotly': [
            'templates/*',
            'resources/js/*'
        ]},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'Plotly = webviz_plotly:Plotly',
            'FilteredPlotly = webviz_plotly:FilteredPlotly'
        ]
    },
    zip_safe=False
)
