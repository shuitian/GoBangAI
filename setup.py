from setuptools import setup, find_packages
import py2exe
setup(
    name = "GoBangAI",
    version = "1.0",
    packages = find_packages(),
    windows=['src\gb\main.py']
)