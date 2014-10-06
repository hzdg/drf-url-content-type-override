from setuptools import setup, find_packages
# Execute emailtools/version.py to add __version__ to setup.py namespace.
# This way, we avoid the django imports that are triggered by importing
# any members of the emailtools module.

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
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
