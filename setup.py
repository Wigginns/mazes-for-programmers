from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mazes",
    version="0.0.1",
    author="Benjamin Cowley",
    # author_email="",
    description="A package implementing mazes for programmers in Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wigginns/mazes-for-programmers",
    project_urls={
        "Bug Tracker": "https://github.com/Wigginns/mazes-for-programmers/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: The Unlicense",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)