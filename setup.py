try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config - {
    'description': 'Virtual Personal Assistant Bot',
    'long description': open('README.md').read(),
    'author': 'Ben Dauer',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dauer.benjamin@gmail.com',
    'version': '0.01a',
    'install_requires': ['nose'], ['flask'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'vpab'
}

setup(**config)
