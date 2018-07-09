from setuptools import setup, find_packages

setup(
    name='webviz_default_theme',
    version='0.1.0a0',
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={'webviz_default_theme': [
        'templates/*',
        'resources/*',
        'resources/img/*',
        'resources/css/*',
        'resources/fonts/*',
        'resources/js/*']},
    install_requires=[
        'jinja2', 'webviz'
    ],
    entry_points={
        'webviz_themes': [
            'default = webviz_default_theme:default_theme'
        ]
    },
    zip_safe=False
)
