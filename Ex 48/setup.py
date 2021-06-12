try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {
    'description': 'Ex 48',
    'author': 'Bruno Diaz',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'name': 'Ex 48'
}

setup(**config)
