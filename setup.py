try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Simple util to convert yaml to json and then invoke jq",
    "author": "Kyle Long",
    "url": "none",
    "download_url": "none",
    "author_email": "uilwen@gmail.com",
    "version": "1",
    "install_requires": [
        "PyYAML",
        "docopt"
    ],
    "scripts": [
        "bin/yq",
    ],
    "name": "yq"
}

setup(**config)
