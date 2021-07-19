#!/usr/bin/env python
""" setup script for delocate package """
from os.path import join as pjoin
from setuptools import setup, find_packages
import codecs

import versioneer

versioneer.VCS = 'git'
versioneer.versionfile_source = pjoin('delocate', '_version.py')
versioneer.versionfile_build = pjoin('delocate', '_version.py')
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'delocate-'

setup(name='delocate',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Move macOS dynamic libraries into package',
      author='Matthew Brett',
      maintainer='Matthew Brett',
      author_email='matthew.brett@gmail.com',
      url='http://github.com/matthew-brett/delocate',
      packages=find_packages(),
      python_requires='>=3.6',
      install_requires=[
          "machomachomangler; sys_platform == 'win32'",
          "bindepend; sys_platform == 'win32'",
          "wheel",
          "six",
          "typing; python_version < '3.5'",
          "typing_extensions",
      ],
      package_data={'delocate.tests':
                    [pjoin('data', '*.dylib'),
                     pjoin('data', '*.txt'),
                     pjoin('data', '*.bin'),
                     pjoin('data', '*.py'),
                     pjoin('data', 'liba.a'),
                     pjoin('data', 'a.o'),
                     pjoin('data', '*.whl'),
                     pjoin('data', 'test-lib'),
                     pjoin('data', '*patch'),
                     pjoin('data', 'make_libs.sh'),
                     pjoin('data', 'icon.ico')]},
      entry_points={
          'console_scripts': [
              'delocate-{} = delocate.cmd.delocate_{}:main'.format(name, name)
              for name in (
                  'addplat',
                  'fuse',
                  'listdeps',
                  'patch',
                  'path',
                  'wheel',
              )
          ]
      },
      license='BSD license',
      classifiers=['Intended Audience :: Developers',
                   "Environment :: Console",
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python',
                   'Operating System :: MacOS :: MacOS X',
                   "Development Status :: 5 - Production/Stable",
                   'Topic :: Software Development :: Libraries :: '
                   'Python Modules',
                   'Topic :: Software Development :: Build Tools'],
      long_description=codecs.open('README.rst', 'r', encoding='utf-8').read(),
      )
