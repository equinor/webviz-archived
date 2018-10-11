from setuptools import setup, find_packages

setup(
    name='webviz_scatter_plot_matrix',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    package_dir={"": "."},
    package_data={
        'webviz_scatter_plot_matrix': []},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz', 'webviz_plotly', 'pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'ScatterPlotMatrix = webviz_scatter_plot_matrix:ScatterPlotMatrix'
        ]
    },
    zip_safe=False
)
