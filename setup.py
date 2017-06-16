from __future__ import absolute_import, print_function, unicode_literals

from setuptools import setup, find_packages

try:
    LONG_DESCRIPTION = open('README.rst').read()
except IOError:
    LONG_DESCRIPTION = ''


setup(
    name='djangorestframework-constant-field',
    version='0.9.1',
    description='A simple Constant Field definition for Django REST Framework',
    long_description=LONG_DESCRIPTION,
    author='Scott Walton',
    author_email='scott.walton@mypebble.co.uk',
    license='Public Domain',
    packages=find_packages(),
    url='https://github.com/mypebble/djangorestframework-constant-field.git',
    install_requires=['django', 'djangorestframework'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
    ]
)
