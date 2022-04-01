# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='gt-align',
    version='0.0.1',
    description='Align full text with image data on line level',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Kay-Michael Würzner',
    author_email='kay-michael.wuerzner@slub-dresden.de',
    license = open('LICENSE').read(),
    packages=find_packages(exclude=('tests', 'docs')),
    #package_data={'gt-align' : []},
    install_requires=open('requirements.txt').read().split('\n'),
    entry_points={
          'console_scripts': [
              'gt-align=gt_align.scripts.gt_align:cli',
          ]
    },
)
