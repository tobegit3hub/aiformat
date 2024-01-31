from setuptools import setup, find_packages

setup(
    name='aiformat',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "aiformat": ["prompt/commands.yaml"],
    },
    install_requires=[
        'click',
        'pyyaml',
        'openai',
        'jinja2'
    ],
    entry_points={
        'console_scripts': [
            'aiformat = aiformat.aiformat:main',
        ],
    },
)