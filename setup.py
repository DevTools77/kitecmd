from setuptools import setup, find_packages

setup(
    name="kitecmd",
    version="0.2",
    author="coltonsr77",
    author_email="coltonsr77@gmail.com",
    description="A simple example CLI command tool for PyPI",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "kitecmd=kitecmd.cli:main",
        ],
    },
    python_requires=">=3.8",
    license="MIT",
)
