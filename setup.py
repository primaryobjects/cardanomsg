# setup.py

from setuptools import setup, find_packages

setup(
    name="cardanomsg",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "blockfrost-python",
        "pycardano"
    ],
    author="Kory Becker",
    author_email="kbecker@primaryobjects.com",
    description="A module to send ADA with a message in the metadata.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/primaryobjects/cardanomsg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
