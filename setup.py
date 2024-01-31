from setuptools import setup, find_packages

setup(
    name='aiformat',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "aiformat": ["prompt/aiformat_command.yaml"],
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