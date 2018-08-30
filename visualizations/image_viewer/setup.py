from setuptools import setup, find_packages

setup(
    name='webviz_image_viewer',
    version='0.1.0',
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={
        'webviz_image_viewer': [
            'templates/*',
            'resources/js/*',
            'resources/css/*'
        ]},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz', 'pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'ImageViewer = webviz_image_viewer:ImageViewer'
        ]
    },
    zip_safe=False
)
