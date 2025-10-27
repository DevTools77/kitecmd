from setuptools import setup, find_packages

setup(
    name="kitecmd",
    version="0.9",
    author="coltonsr77",
    description="A CLI tool with update checking and other tools.",
    packages=find_packages(include=["kitecmd", "kitecmd.*"]),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "kitecmd=kitecmd.cli:main",
        ],
    },
    include_package_data=True,
    python_requires=">=3.9",
)
