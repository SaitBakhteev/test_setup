from setuptools import find_packages,setup

setup(name='lib_',
      packages=find_packages(include='lib5_'),
      version='0.0.1',
      description='myProg',
      author='I',
      license='X',
      install_requires=[],
      setup_requires=['pytest-runner'],
      test_require=['pytest>=4.4.1'],
      test_suite='test_lib',
      )