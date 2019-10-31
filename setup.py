#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='Unifile',
    version='0.1',
    author="heavyblack",
    author_email="heavyblack@gmail.com",
    packages=['unifile'],
    license='GNU v3',
    url='https://github.com/heavyblack/unifile',
    keywords="file yaml json txt",
    description="For save settings or file load dump data",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    install_requires=[
        'pyaml', 'pandas', 'PyPDF2', 'openpyxl'
    ],
    project_urls={
        "Source Code": "https://github.com/heavyblack/unifile",
    },
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]

)
