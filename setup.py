from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.10'
DESCRIPTION = 'This is a package to extract the Non-dimensional factors of fracture mechanics.'

# Setting up
setup(
    name="fracmechfact",
    version=VERSION,
    author="Hrushikesh Sahasrabuddhe",
    author_email="<sahasrabuddhehrushi.99@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'fracture mechanics', 'geometric factor'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
