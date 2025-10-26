from setuptools import setup, find_packages

setup(
    name="kitecmd",
    version="0.5",
    author="coltonsr77",
    description="A simple CLI example for PyPI that runs anywhere",
    packages=find_packages(include=["kitecmd", "kitecmd.*"]),
    entry_points={
        "console_scripts": [
            "kitecmd=kitecmd.cli:main",
        ],
    },
    include_package_data=True,
    python_requires=">=3.8",
)
