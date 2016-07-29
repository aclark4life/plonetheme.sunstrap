from setuptools import find_packages
from setuptools import setup

VERSION = '0.0.7'

setup(author='Alex Clark',
      author_email='aclark@aclark.net',
      classifiers=[
          'Framework :: Plone :: 4.3',
          'Programming Language :: Python :: 2.7',
      ],
      description='Plone theme',
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      keywords='Bootstrap Diazo Modern Plone Sunburst Theme Theming',
      license='GPL2',
      include_package_data=True,
      install_requires=[
          'setuptools',
      ],
      long_description=open('README.rst').read() + '\n' +
      open('CHANGES.rst').read(),
      name='plonetheme.sunstrap',
      namespace_packages=[
          'plonetheme',
      ],
      packages=find_packages(),
      test_suite='',
      url='https://github.com/aclark4life/plonetheme.sunstrap',
      version=VERSION,
      zip_safe=False, )
