from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Jot",
    version="0.1.0-.pre2",
    author="ZenSharp",
    author_email="andtechstudios@gmail.com",
    description="A CLI for journaling.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zensharp/jot",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['jot=src.jot:main'],
    }
)