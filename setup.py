import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
# Execute emailtools/version.py to add __version__ to setup.py namespace.
# This way, we avoid the django imports that are triggered by importing
# any members of the emailtools module.


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '-s']
        self.test_suite = True

    def run_tests(self):
        import pytest
        # Make sure this package's tests module gets priority.
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='django-rest-url-override-content-negotiation',
    version='0.0.1',
    author='Chris McKenzie',
    author_email='me@christophermckenzie.com',
    packages=find_packages(),
    include_package_data=False,
    description='The name says it all.',
    license='LICENSE.txt',
    long_description=open('README.rst').read(),
    zip_safe=False,
    tests_require=[
        'pytest',
        'djangorestframework',
    ],
    install_requires=[
        'Django>=1.6.5'
    ],
    cmdclass={
        'test': PyTest
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
