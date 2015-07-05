__author__ = 'Allen Goodman'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from setuptools.command.test import test
except ImportError:
    command = {}
else:
    class PyTest(test):
        def __init__(self, dist, **kw):
            super().__init__(dist, **kw)

            self.test_args = []

            self.test_suite = []

        def finalize_options(self):
            test.finalize_options(self)

        def run_tests(self):
            from pytest import main

            errno = main(self.test_args)

            raise SystemExit(errno)

    command = {'test': PyTest}

setup(
    name='westernization',
    packages=['westernization'],
    data_files=[('', ['README.rst'])],
    version='1.0.0',
    description='analyze and annotate western blots',
    long_description='…',
    license='MIT',
    author='Allen Goodman',
    author_email='allen.goodman' '@' 'icloud.com',
    maintainer='Allen Goodman',
    maintainer_email='allen.goodman' '@' 'icloud.com',
    url='https://github.com/0x00B1/westernization',
    tests_require=[
        'pytest >= 2.3.0'
    ],
    extras_require={'doc': ['Sphinx >=1.0']},
    classifiers=[],
    cmdclass=command
)
