try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'project description',
    'author':'your name',
    'url':'URL to get the project at where',
    'download_url':'where to download the project',
    'autor_email':'your email address',
    'version':'0.1.0',
    'install_requires':['nose'],
    'packages':['project'],
    'scripts':[],
    'name':'project-name',
    'license':'MIT'
}

setup(**config)
