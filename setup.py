from setuptools import setup, find_packages

VERSION = '0.7.2'

setup(
    name='httplib2',
    version=VERSION, 
    author='Joe Gregorio',
    author_email='joe@bitworking.org',
    url='https://github.com/bryanhelmig/httplib2-bigcerts/',
    download_url='https://github.com/bryanhelmig/httplib2-bigcerts/',
    description='A comprehensive HTTP client library.',
    license='MIT',
    packages = find_packages(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    keywords = 'httplib2 http certs',
    zip_safe = True,
    install_requires=['distribute']
)
