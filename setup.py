
from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="scalg",
    version="0.1.4",
    description="Analyse data file using a range based procentual proximity algorithm and calculate the linear maximum likelihood estimation.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/markmelnic/Scoring-Algorithm",
    author="Mark Melnic",
    author_email="commerce.markmelnic@gmail.com",
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
        ]
    },
)
