from setuptools import setup, find_packages

setup(
    name="kitecmd",
    version="0.3",
    author="coltonsr77",
    description="A simple CLI example for PyPI",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "kitecmd=kitecmd.cli:main",
        ],
    },
    python_requires=">=3.8",
)
