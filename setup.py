from setuptools import setup

setup(
    name='web-scraper',
    version='1.0.0',
    description='Simple web scraper',
    url='https://github.com/hojp7874/web-scraper.git',
    author='hongjinpyo',
    author_email='hojp7874@gmail.com',
    license='hongjinpyo',
    packages=['web_scraper'],
    install_requires=[
        'beautifulsoup4==4.9.3',
        'bs4==0.0.1',
        'certifi==2021.5.30',
        'chardet==4.0.0',
        'idna==2.10',
        'requests==2.25.1',
        'soupsieve==2.2.1',
        'urllib3==1.26.5',
    ]
)