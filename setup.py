import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyang-jsontree-plugin',
    version='0.2',
    description=('A pyang plugin to produce a JSON representation of module trees for use in graph libraries'),
    long_description=read('README.md'),
    packages=['jsontree'],
    author='Carl Moberg',
    author_email='camoberg@cisco.com',
    license='New-style BSD',
    url='https://github.com/cmoberg/pyang-jsontree-plugin',
    install_requires=['pyang'],
    include_package_data=True,
    keywords=['yang', 'extraction', 'json'],
    classifiers=[],
    entry_points={'pyang.plugin': 'module_jsontree_plugin=modulecatalog.modulecatalog:pyang_plugin_init'}
)