"""packaging for helloworld."""

from setuptools import find_packages, setup

setup(
    name='train',
    version='1.0.6.dev1',
    packages=find_packages(),
    url='',
    license='',
    author='Lukas Schmid',
    author_email='lukas.m.schmid@gmail.com',
    description='model train application',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
