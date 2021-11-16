from setuptools import setup, find_packages
from os.path import abspath, dirname, join

this_dir = abspath(dirname(__file__))
    
with open(join(this_dir, "requirements.txt")) as f:
    requirements = f.read().split("\n")

setup(
        name="example_package",
        version="1.0",
        description="",
        url="https://github.com/JosephPB/example_package/",
        author="Joseph Aylett-Bullock",
        author_email='joseph@unglobalpulse.org',
        license="MIT license",
        install_requires=requirements,
        packages=find_packages(),
)

