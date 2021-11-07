from setuptools import setup, find_packages

setup(
    name="ddr",
    version="0.2",
    description="Functions for implementing and exploring Distributed Dictionary Representation",
    author="Joe Hoover, Georgios Chochlakis",
    author_email="jehoover@usc.edu, chochlak@usc.edu",
    license="USC",
    packages=find_packages(),
    package_data={"ddr": ["*.pdf", "*.txt"]},
    zip_safe=False,
    install_requires=[
        "numpy==1.21.4",
        "pandas==1.3.4",
        "cython==0.29.24",
        "gensim==4.1.2",
    ],
)
