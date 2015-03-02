#!/usr/bin/env python

from setuptools import setup

setup(
    name='mschap',
    version='1.0.1',
    author='bit0rez',
    author_email='b1t0r3z@gmail.com',
    description='Copy of mschap library for python. Library copied from IBS project (http://sourceforge.net/projects/ibs/).',
    long_description=open('README.md').read(),
    url='https://github.com/xjaner/mschap-python',
    packages=['mschap'],
    license='GNU General Public License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
