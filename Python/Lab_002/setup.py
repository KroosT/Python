from setuptools import find_packages, setup
from os.path import join, dirname

setup(
    name='Lab_002',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'readme.txt')).read(),
    entry_points={
        'console_scripts':
            ['file_generating = 2.file_generating.file_generator:main',
             'to_json = to_json.to_json:main',
             'n-vector = 4.nvector.nvector:main',
             'logger = 5.logger.logger:main',
             'defaultdict = 6.defaultdict.defaultdict:main',
             'metaclass = 7.metaclass.metaclass:main',
             'cached = 8.decorator.cached:main',
             'xrange = 9.xrange.xrange:main',
             'sequence = 10.sequence.sequence:main']
    }
)
