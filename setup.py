from setuptools import setup, find_packages
from codecs import open

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='vtex',
    version='0.1.4',
    license="MIT",
    description='VTEX API Wrapper for Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Leandro Meili',
    author_email='leandro.meili@gmail.com',
    url='https://github.com/lmeilibr/vtex',
    packages=find_packages(exclude=("test",)),
    install_requires=['requests'],
    setup_requires=['wheel'],
)
