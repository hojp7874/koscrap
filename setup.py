from setuptools import setup, find_packages

setup(
    name='web-scraper',
    version='1.0.0',
    description='Simple web scraper',
    url='https://github.com/hojp7874/web-scraper.git',
    author='hongjinpyo',
    author_email='hojp7874@gmail.com',
    license='hongjinpyo',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'bs4==0.0.1',
        'requests==2.26.0',
    ]
)