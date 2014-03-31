from setuptools import setup

config = {
    name='torrent_handler',
    version='0.1',
    description='Transmission Remote frontend.',
    url='http://github.com/patwaw/torrent_handler',
    author='patwaw',
    author_email='patwawrz@gmail.com',
    license='MIT',
    packages=['torrent_handler'],
    install_requires=['transmissionrpc']
    zip_safe=False 
}

setup(**config)