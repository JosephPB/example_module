from setuptools import setup, find_packages, Extension
from os.path import abspath, dirname, join

this_dir = abspath(dirname(__file__))
    
with open(join(this_dir, "requirements.txt")) as f:
    requirements = f.read().split("\n")

setup(
        name="example_module",
        version="1.0",
        description="",
        url="https://github.com/JosephPB/example_module/",
        author="Joseph Aylett-Bullock",
        author_email='joseph@unglobalpulse.org',
        license="MIT license",
        install_requires=requirements,
        packages = ["example_module"],
)

