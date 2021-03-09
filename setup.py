from setuptools import setup, find_packages
from scalg.version import __version__

setup(
    name="scalg",
    version=__version__,
    description="A Python list scoring algorithm. Analyse data file using a range based procentual proximity algorithm and calculate the linear maximum likelihood.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/markmelnic/Scoring-Algorithm",
    author="Mark Melnic",
    author_email="commerce.markmelnic@gmail.com",
    license="MIT",
    python_requires='==3.*',
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": []},
)
