#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = []

setup(
    author="Alejandro Alcantar Medel",
    author_email='A01688416@tec.mx',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A model is sought that at least has an average of 65% in accuracy or higher",
    entry_points={
        'console_scripts': [
            'integratorproject=integratorproject.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='integratorproject',
    name='integratorproject',
    packages=find_packages(include=['integratorproject', 'integratorproject.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/AlejandroAlcantar/integratorproject',
    version='0.1.0',
    zip_safe=False,
)
