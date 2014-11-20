try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    config = {
        'description': 'NER and IE Project',
        'author': 'Zexi Mao',
        'url': 'https://github.com/KyleMao/simple-ner-ie',
        'download_url': 'https://github.com/KyleMao/simple-ner-ie.git',
        'author_email': 'zexim@cs.cmu.edu',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': [],
        'scripts': [],
        'name': 'simple-ner-ie'
    }

    setup(**config)
