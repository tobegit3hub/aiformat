from setuptools import setup, find_packages

setup(
    name='aiformat',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pyyaml',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'aiformat = aiformat.aiformat:main',
        ],
    },
)