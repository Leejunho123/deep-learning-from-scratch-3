import os
import io
from setuptools import find_packages, setup
from dezero import __version__


def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme
    
setup(name='dezero',
      version=__version__,
      license='MIT License',
      install_requires=['numpy'],
      description='Deep Learning Framework from Zero',
      author='Koki Saitoh',
      author_email='koki0702@gmail.com',
      url='',
      packages=['dezero'],
      )

