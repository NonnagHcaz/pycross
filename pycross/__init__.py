import datetime

__version__ = '0.1.0'
__version_info__ = tuple([int(num) for num in __version__.split('.')])
__title__ = 'pycross'
__summary__ = 'Nonogram puzzle generator'
__uri__ = ''
__author__ = 'Zach Gannon'
__email__ = 'zachgannon93@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) {} {}'.format(
    datetime.datetime.now().strftime('%Y'), __author__)
__classifiers__ = '\n'.join([
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Software Development :: Libraries :: Python Modules'
])
