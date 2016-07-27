from setuptools import find_packages
from setuptools import setup

VERSION='0.0.2'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[],
    description='',
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    keywords='',
    license='',
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    long_description=open('README.rst').read() + '\n' + open('CHANGES.rst').read(),
    name='plonetheme.sunstrap',
    namespace_packages=[
        'plonetheme',
    ],
    packages=find_packages(),
    test_suite='',
    url='',
    version=VERSION,
    zip_safe=False,
)
