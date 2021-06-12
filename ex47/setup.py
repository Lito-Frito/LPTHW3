try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Sample game for testing purposes',
    'author': 'Bruno Diaz',
    'url': 'www.crc8109.com',
    'download_url': 'githug.com/crc8109',
    'author_email': 'crc8109@pm.me',
    'version': '0.1',
    'install_requires': ['noses'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex47.py'
}

setup(**config)
