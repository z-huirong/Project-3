#!/usr/bin/env python

from setuptools import setup
 
setup(
    name="Helllohuirong",
    version="0.1",
    scripts=['data1.py'],
    data_files = [('.', ['data-1.csv'])],
    install_requires=['matplotlib', 'pandas'],
    author="Me",
    author_email="zhuhuirong_sh@hotmail.com",
    description="This is my first Package",
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]
 )